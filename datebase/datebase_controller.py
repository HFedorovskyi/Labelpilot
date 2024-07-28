from PySide6.QtCore import QObject
from datebase.datebase_main import get_db_session
from datebase.datebase_main import Nomenclature, Pallet, Boxes, Pack
from datetime import datetime
from PySide6.QtWidgets import QTreeWidgetItem, QAbstractItemView


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
            text = self.ui.ArticletextEdit.text()
            nomenclature = db.query(Nomenclature).filter(Nomenclature.article == text).first()
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

    @staticmethod
    def generate_pallet_number(last_pallet_number):
        date_now = datetime.now()
        formated_date = date_now.strftime("%d%m%Y")
        new_pallet_number = f'46{formated_date}{int(last_pallet_number[8:]) + 1}'
        return new_pallet_number

    def get_last_pallet_number(self):
        with get_db_session() as db:
            last_pallet = db.query(Pallet.number).order_by(Pallet.id.desc()).limit(1).first()[0]
            if last_pallet:
                return last_pallet
            return None

    def new_pallet_number(self):
        last_pallet_number = self.get_last_pallet_number()
        if last_pallet_number:
            return self.generate_pallet_number(last_pallet_number)
        else:
            date_now = datetime.now()
            formated_date = date_now.strftime("%d%m%Y")
            return f'46{formated_date}00000000'

    def new_pack_number(self):
        with get_db_session() as db:
            last_pack_number = db.query(Pack).order_by(Pack.id.desc()).limit(1).first()
            if last_pack_number:
                last_pack_number = int(last_pack_number.number) + 1
                return f'{last_pack_number:012d}'
            else:
                return f'{0:012d}'

    def new_box_number(self):
        with get_db_session() as db:
            last_box_number = db.query(Boxes).order_by(Boxes.id.desc()).limit(1).first()
            if last_box_number:
                last_box_number = int(last_box_number.number) + 1
                return f'{last_box_number:012d}'
            else:
                return f'{0:012d}'

    def close_box(self):
        pass

    def write_to_ContainerstreeWidget(self, weight_netto, weight_brutto):
        '''Запись в базу данных и таблицу отображения промаркированных продуктов'''
        with get_db_session() as db:
            number_pack = self.new_pack_number()
            current_nomenclature = self.ui.NomenclatureComboBox.currentText()
            current_article = db.query(Nomenclature.article).filter(Nomenclature.name == current_nomenclature).first()
            pallet_number = self.get_last_pallet_number()
            current_box = db.query(Boxes.number).order_by(Boxes.id.desc()).limit(1).first()
            if current_box:
                box_number = current_box.number
            else:
                box_number = self.new_box_number()

            if self.pack_count >= db.query(Nomenclature).filter(
                    Nomenclature.name == current_nomenclature).first().close_box_counter:
                status_box = db.query(Boxes).order_by(Boxes.id.desc()).limit(1).first()
                status_box.is_open = False
                box_number = self.new_box_number()

                box_row = Boxes(pallete_id=db.query(Pallet).order_by(Pallet.id.desc()).first().id,
                                number=box_number,
                                created_at=datetime.now(),
                                is_open=True)
                db.add(box_row)
                db.commit()
                self.pack_count = 0

            created_at = datetime.now()
            formated_created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
            row = QTreeWidgetItem(self.ui.ContainerstreeWidget)
            row.setText(0, number_pack)
            row.setText(1, current_article.article)
            row.setText(2, current_nomenclature)
            row.setText(3, weight_netto)
            row.setText(4, weight_brutto)
            row.setText(5, box_number)
            row.setText(6, pallet_number)
            row.setText(7, formated_created_at)
            self.ui.ContainerstreeWidget.scrollToItem(row, QAbstractItemView.PositionAtBottom)

            pack_row = Pack(
                number=number_pack,
                created_at=created_at,
                box_id=db.query(Boxes.id).order_by(Boxes.id.desc()).limit(1).first().id,
                nomenclature_id=db.query(Nomenclature.id).filter(Nomenclature.name == current_nomenclature).first().id,
                weight_netto=weight_netto,
                weight_brutto=weight_brutto,
                status='created'

            )
            db.add(pack_row)
            db.commit()

            self.pack_count += 1
