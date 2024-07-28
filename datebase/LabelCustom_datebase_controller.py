from PySide6.QtCore import QObject
from datebase.datebase_main import get_db_session
from datebase.datebase_main import Nomenclature, Pallet, Boxes, Pack
from datetime import datetime
from PySide6.QtWidgets import QTreeWidgetItem, QAbstractItemView
from datebase.datebase_communications import WorkWithPack


class LabelCustomDbController(QObject):
    '''Класс для заполнения основных полей на виджете "Маркировка без задания" с базы данных'''

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.load_all_nomenclature()
        self.search_nomenclature_by_article()
        self.func_connect()
        self.set_weight_container()
        if not self.check_db_empty():
            self.set_article_like_nomenclature()

    def func_connect(self):
        self.ui.ArticletextEdit.textChanged.connect(self.search_nomenclature_by_article)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.set_weight_container)
        self.ui.NomenclatureComboBox.currentTextChanged.connect(self.set_article_like_nomenclature)

    def load_all_nomenclature(
            self):  #Выгрузка всей номенклатуры с базы и добавление в комбобокс для выбора номенклатуры
        with get_db_session() as db:
            nomenclatures = db.query(Nomenclature.name).all()
            for nomenclature in nomenclatures:
                self.ui.NomenclatureComboBox.addItem(nomenclature[0])

    def search_nomenclature_by_article(self):  # Поиск номенклатуры по артикулу
        with get_db_session() as db:
            article = self.ui.ArticletextEdit.text()
            nomenclature = db.query(Nomenclature).filter(Nomenclature.article == article).first()
            if nomenclature:
                self.ui.NomenclatureComboBox.setCurrentText(nomenclature.name)

    def set_article_like_nomenclature(self):
        with get_db_session() as db:
            current_nomenclature = self.ui.NomenclatureComboBox.currentText()
            nomenclature = db.query(Nomenclature).filter(Nomenclature.name == current_nomenclature).first()
            self.ui.ArticletextEdit.setText(nomenclature.article)

    def set_weight_container(self):
        with get_db_session() as db:
            weigh_container = db.query(Nomenclature).filter(
                Nomenclature.name == self.ui.NomenclatureComboBox.currentText()).first()
            if weigh_container:
                self.ui.conteinerWeightTextBrowser.setText(
                    str(weigh_container.box_container.weight + weigh_container.portion_container.weight))

    @staticmethod
    def check_db_empty():
        with get_db_session() as db:
            if db.query(Nomenclature).count() == 0:
                return True
            return False


class FillTreeWidgetDbController(QObject):

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.set_ui()
        self.pack_worker = WorkWithPack(self.ui)
        self.pack_count = 0

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
            self.pack_worker.new_pack_number(weight_netto, weight_brutto)
            created_at = datetime.now()
            formated_created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
            row = QTreeWidgetItem(self.ui.ContainerstreeWidget)
            row.setText(0, self.pack_worker.current_pack_number)
            row.setText(1, self.pack_worker.boxes_worker.get_current_nomenclature().article)
            row.setText(2, self.pack_worker.boxes_worker.get_current_nomenclature().name)
            row.setText(3, weight_netto)
            row.setText(4, weight_brutto)
            row.setText(5, self.pack_worker.boxes_worker.current_box_number)
            row.setText(6, self.pack_worker.boxes_worker.pallet_worker.current_pallet)
            row.setText(7, formated_created_at)
            self.ui.ContainerstreeWidget.scrollToItem(row, QAbstractItemView.PositionAtBottom)

