from PySide6.QtCore import QObject, Qt, Slot, Signal
from PySide6.QtGui import QColor
from datebase.datebase_main import get_db_session
from datebase.datebase_main import Nomenclature, Boxes
from datetime import datetime
from PySide6.QtWidgets import QTreeWidgetItem, QAbstractItemView
from datebase.datebase_communications import WorkWithPack, WorkWithBoxes, WorkWithPallet
from views.close_box_error import CloseBoxError
from app_logging.logging_config import logger


class LabelCustomDbController(QObject):
    '''Класс для заполнения основных полей на виджете "Маркировка без задания" с базы данных'''

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.error_window = CloseBoxError()
        self.load_all_nomenclature()
        self.search_nomenclature_by_article()
        self.current_nomenclature_index = self.ui.NomenclatureComboBox.currentIndex()
        self.func_connect()
        self.set_weight_container()
        self.set_max_pack_in_box()
        if not self.check_db_empty():
            self.set_article_like_nomenclature()

    def func_connect(self):
        self.ui.ArticletextEdit.textChanged.connect(self.search_nomenclature_by_article)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.set_weight_container)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.check_box_open)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.set_max_pack_in_box)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.set_article_like_nomenclature)

    def load_all_nomenclature(
            self):  #Выгрузка всей номенклатуры с базы и добавление в комбобокс для выбора номенклатуры
        with get_db_session() as db:
            nomenclatures = db.query(Nomenclature.name).all()
            for nomenclature in nomenclatures:
                self.ui.NomenclatureComboBox.addItem(nomenclature[0])

    def get_db_nomenclature(self):
        current_nomenclature = self.ui.NomenclatureComboBox.currentText()
        with get_db_session() as db:
            db_current_nomenclature = db.query(Nomenclature).filter(Nomenclature.name == current_nomenclature).first()
            return db_current_nomenclature

    def check_box_open(self):
        with get_db_session() as db:
            try:
                check_box_open = db.query(Boxes).order_by(Boxes.id.desc()).first().status
            except Exception as e:
                check_box_open = False

            if check_box_open == 'Open':
                self.error_window.current_page(4)
                obj = self.ui.indicationWeightNettotextBrowser
                self.error_window.setGeometry(obj.mapToGlobal(obj.rect().bottomLeft()).x() - 80,
                                              obj.mapToGlobal(obj.rect().bottomLeft()).y(), 400, 300)
                self.error_window.show()
                self.ui.NomenclatureComboBox.setCurrentIndex(self.current_nomenclature_index)

    def search_nomenclature_by_article(self):
        with get_db_session() as db:
            article = self.ui.ArticletextEdit.text()
            nomenclature = db.query(Nomenclature).filter(Nomenclature.article == article).first()
            if nomenclature:
                self.ui.NomenclatureComboBox.setCurrentText(nomenclature.name)
                self.current_nomenclature_index = self.ui.NomenclatureComboBox.currentIndex()

    def set_article_like_nomenclature(self):
        nomenclature = self.get_db_nomenclature()
        self.ui.ArticletextEdit.setText(nomenclature.article)

    def set_max_pack_in_box(self):
        nomenclature = self.get_db_nomenclature()
        self.ui.maxPackInBoxLabel.setText(str(nomenclature.close_box_counter))

    def set_weight_container(self):
        with get_db_session() as db:
            nomenclature = db.query(Nomenclature).filter(
                Nomenclature.name == self.ui.NomenclatureComboBox.currentText()).first()
            if nomenclature:
                self.ui.containerWeightLabel.setText(
                    str(nomenclature.box_container.weight + nomenclature.portion_container.weight))

    @staticmethod
    def check_db_empty():
        with get_db_session() as db:
            if db.query(Nomenclature).count() == 0:
                return True
            return False


class WorkingWithPacksController(QObject):
    packaging_added = Signal(int)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.set_ui()
        self.pallet_worker = WorkWithPallet()
        self.boxes_worker = WorkWithBoxes(self.ui, self.pallet_worker)
        self.pack_worker = (
            WorkWithPack(self.ui, self.boxes_worker))
        self.pack_count = 0
        self.pack_worker.closer_box.connect(self.on_update_table_complete_box)
        self.boxes_worker.pallet_closer.connect(self.on_update_table_complete_pallet)
        self.packaging_added.connect(self.update_currentPackInBoxLabel)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.boxes_worker.update_pack_in_box)
        self.change_max_box_in_label()
        self.ui.MaxBoxOnPalletLineEdit.editingFinished.connect(self.change_max_box_in_label)

    def set_ui(self):
        self.ui.ContainerstreeWidget.setColumnWidth(0, 130)
        self.ui.ContainerstreeWidget.setColumnWidth(1, 70)
        self.ui.ContainerstreeWidget.setColumnWidth(2, 320)
        self.ui.ContainerstreeWidget.setColumnWidth(3, 70)
        self.ui.ContainerstreeWidget.setColumnWidth(4, 70)
        self.ui.ContainerstreeWidget.setColumnWidth(5, 120)
        self.ui.ContainerstreeWidget.setColumnWidth(6, 160)
        self.ui.ContainerstreeWidget.setColumnWidth(7, 100)
        self.ui.printPortionBtn.clicked.connect(lambda: self.write_to_ContainerstreeWidget(
            self.ui.indicationWeightNettotextBrowser.toPlainText(),
            self.ui.indicationWeightBruttoBrowser.toPlainText()))

    def write_to_ContainerstreeWidget(self, weight_netto, weight_brutto):
        self.pack_worker.new_pack(weight_netto, weight_brutto)
        created_at = datetime.now()
        formated_created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
        row = QTreeWidgetItem(self.ui.ContainerstreeWidget)
        row.setText(0, self.pack_worker.current_pack_number)
        row.setText(1, self.pack_worker.boxes_worker.get_current_nomenclature().article)
        row.setText(2, self.ui.NomenclatureComboBox.currentText())
        row.setText(3, weight_netto)
        row.setText(4, weight_brutto)
        row.setText(5, self.pack_worker.boxes_worker.current_box_number)
        row.setBackground(5, QColor(255, 189, 136))
        row.setText(6, self.pack_worker.boxes_worker.pallet_worker.current_pallet)
        row.setBackground(6, QColor(255, 189, 136))
        row.setText(7, formated_created_at)
        self.ui.ContainerstreeWidget.scrollToItem(row, QAbstractItemView.PositionAtBottom)
        self.packaging_added.emit(self.pack_worker.pack_counter)

    def fill_ContainerstreeWidget(self):
        last_twenty_pack_data = self.pack_worker.get_twenty_last_pack()
        if last_twenty_pack_data:
            for item in reversed(last_twenty_pack_data):
                row = QTreeWidgetItem(self.ui.ContainerstreeWidget)
                row.setText(0, str(item.number))
                row.setText(1, item.nomenclature.article)
                row.setText(2, item.nomenclature.name)
                row.setText(3, str(item.weight_netto))
                row.setText(4, str(item.weight_brutto))
                row.setText(5, item.boxes.number if item.boxes else None)
                row.setBackground(5, QColor(168, 228, 160))
                row.setText(6, item.boxes.pallet.number if item.boxes else None)
                row.setBackground(6, QColor(168, 228, 160))
                row.setText(7, item.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                self.ui.ContainerstreeWidget.addTopLevelItem(row)

            self.ui.ContainerstreeWidget.scrollToItem(row, QAbstractItemView.PositionAtBottom)

    @Slot()
    def on_update_table_complete_box(self):
        logger.debug('on_update_table_complete_box started!')
        self.change_color_closed_box(self.pack_worker.boxes_worker.current_box_number)

    @Slot()
    def on_update_table_complete_pallet(self):
        logger.debug('on_update_table_complete_pallet started!')
        self.change_color_pallet(self.pallet_worker.current_pallet)

    def change_color_closed_box(self, box_number):
        for item in self.ui.ContainerstreeWidget.findItems(box_number, Qt.MatchFlag.MatchExactly, 5):
            item.setBackground(5, QColor(168, 228, 160))

    def change_color_pallet(self, pallet_number):
        for item in self.ui.ContainerstreeWidget.findItems(pallet_number, Qt.MatchFlag.MatchExactly, 6):
            item.setBackground(6, QColor(168, 228, 160))

    @Slot(int)
    def update_currentPackInBoxLabel(self, pack_counter):
        self.ui.currentPackInBoxLabel.setText(str(pack_counter))

    def change_max_box_in_label(self):
        self.ui.MaxBoxInPalletLabel.setText(str(self.ui.MaxBoxOnPalletLineEdit.text()))
