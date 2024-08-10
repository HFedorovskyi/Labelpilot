from app_logging.logging_config import logger
from datebase.datebase_main import get_db_session
from datebase.datebase_main import Nomenclature, Pallet, Boxes, Pack
from datetime import datetime
from sqlalchemy.orm import joinedload
from PySide6.QtCore import Signal, QObject, Slot, QTimer
from views.close_box_error import CloseBoxError


class WorkWithPallet:

    def __init__(self):
        self.current_pallet = self.get_last_pallet()
        self.pallet_status = None

    def new_pallet(self, last_pallet_number: str):
        logger.info(f"Last pallet number : {last_pallet_number}")
        self.pallet_status = 'Open'
        date_now = datetime.now()
        formated_date = date_now.strftime("%d%m%Y")
        new_pallet_number = f'46{formated_date}{(int(last_pallet_number[10:]) + 1):007d}'
        self.current_pallet = new_pallet_number
        logger.info(f"New pallet number : {self.current_pallet}")
        self.add_db_new_pallet(self.current_pallet)

    @staticmethod
    def new_pallet_number():
        date_now = datetime.now()
        formated_date = date_now.strftime("%d%m%Y")
        return f'46{formated_date}0000000'

    def get_last_pallet(self):
        with get_db_session() as db:
            last_pallet = db.query(Pallet.number).order_by(Pallet.id.desc()).limit(1).first()
            if last_pallet:
                return last_pallet.number
            new_pallet_number = self.new_pallet_number()
            self.add_db_new_pallet(new_pallet_number)
            return new_pallet_number

    @staticmethod
    def add_db_new_pallet(new_pallet_number):
        with get_db_session() as db:
            new_pallet = Pallet(
                number=new_pallet_number
            )
            db.add(new_pallet)
            db.commit()


class WorkWithBoxes(QObject):
    pallet_closer = Signal(str)
    complete_adding_pallet = Signal()

    def __init__(self, ui, pallet_worker):
        super().__init__()
        self.box_status = None
        self.ui = ui
        self.box_on_pallet = int(self.ui.MaxBoxOnPalletLineEdit.text())
        self.box_counter = 0
        self.current_box_number = self.last_box()
        self.pallet_worker = pallet_worker
        self.pack_in_box = self.get_current_nomenclature().close_box_counter
        self.error_window = CloseBoxError()
        self.ui.closePalletButton.clicked.connect(self.close_pallet)
        self.complete_adding_pallet.connect(self.on_complete_adding_box)

    def new_box(self):
        self.box_status = 'Open'
        logger.debug(f"Last box number : {self.current_box_number}")
        new_box_number = int(self.current_box_number) + 1
        self.current_box_number = f'{new_box_number:012d}'
        logger.debug(f"New box number : {self.current_box_number}")
        self.add_db_new_box(self.current_box_number)
        self.box_counter += 1

    def update_pack_in_box(self):
        self.pack_in_box = self.get_current_nomenclature().close_box_counter
        return self.pack_in_box

    def close_pallet(self):

        if self.box_status == 'Closed' and self.box_counter > 0:
            self.ui.stackedWidget_4.setCurrentIndex(1)
            logger.debug(f"Close pallet beggining")
            with get_db_session() as db:
                update_status_pallette = db.query(Pallet).filter(
                    Pallet.number == self.pallet_worker.current_pallet).first()
                update_status_pallette.status = 'Closed'
                update_status_pallette.updated_at = datetime.now()
                db.commit()
            self.box_counter = 0
            self.pallet_worker.pallet_status = 'Closed'
            QTimer.singleShot(0, lambda: self.complete_adding_pallet.emit())

        elif self.box_counter == 0:
            self.show_error_window(2)

        else:
            self.show_error_window(0)

    def last_box(self):
        with get_db_session() as db:
            last_box_number = db.query(Boxes).order_by(Boxes.id.desc()).limit(1).first()
            if last_box_number:
                return last_box_number.number
            else:
                return f'{0:012d}'

    def change_close_box_status(self, box_number: str):
        self.box_status = 'Closed'
        with get_db_session() as db:
            change_box = db.query(Boxes).filter(Boxes.number == box_number).first()
            change_box.status = self.box_status
            change_box.updated_at = datetime.now()

            db.commit()

    def add_db_new_box(self, box_number: str):
        with get_db_session() as db:
            box_row = Boxes(pallete_id=db.query(Pallet.id).order_by(Pallet.id.desc()).first().id,
                            number=box_number,
                            created_at=datetime.now(),
                            )
            db.add(box_row)
            db.commit()

    def get_current_nomenclature(self):
        with get_db_session() as db:
            get_nomenclature = self.ui.NomenclatureComboBox.currentText()
            current_nomenclature = db.query(Nomenclature).filter(Nomenclature.name == get_nomenclature).first()
            return current_nomenclature

    @Slot()
    def on_complete_adding_box(self):
        logger.debug(f"Signal complete!")
        self.pallet_closer.emit(self.pallet_worker.current_pallet)

    def show_error_window(self, page_number: int):
        self.error_window.current_page(page_number)
        obj = self.ui.indicationWeightNettotextBrowser
        self.error_window.setGeometry(obj.mapToGlobal(obj.rect().bottomLeft()).x() - 80,
                                      obj.mapToGlobal(obj.rect().bottomLeft()).y(), 400, 300)
        self.error_window.show()


class WorkWithPack(QObject):
    closer_box = Signal(str)
    complete_adding_pack = Signal()

    def __init__(self, ui, boxes_worker):
        super().__init__()
        self.ui = ui
        self.box_status = None
        self.boxes_worker = boxes_worker
        self.current_pack_number = self.get_last_pack()
        self.pack_counter = 0
        self.error_window = CloseBoxError()
        self.complete_adding_pack.connect(self.complete_add_pack)
        self.ui.closeBoxButton.clicked.connect(self.close_box)
        logger.info(f'Class name - {__class__.__name__}: Initialization with attributes:'
                    f'current pack number :{self.current_pack_number} /'
                    f'pack counter: {self.pack_counter}')

    def get_last_pack(self):
        with get_db_session() as db:
            last_pack_number = db.query(Pack).order_by(Pack.id.desc()).limit(1).first()
            if last_pack_number:
                return last_pack_number.number
            else:
                return f'{0:012d}'

    def new_pack(self, weight_netto: float, weight_brutto: float):
        if self.ui.stackedWidget_3.currentIndex() != 0:
            self.ui.stackedWidget_3.setCurrentIndex(0)

        if self.ui.stackedWidget_4.currentIndex() != 0:
            self.ui.stackedWidget_4.setCurrentIndex(0)

        if self.boxes_worker.box_counter == 0:
            logger.debug(f'Condition of creating new pallet success.')
            self.boxes_worker.pallet_worker.new_pallet(self.boxes_worker.pallet_worker.current_pallet)

        if self.pack_counter == 0:
            logger.debug(f'Condition of create new box success.')
            self.boxes_worker.new_box()
            self.ui.CurrentBoxOnPalletLabel.setText(str(self.boxes_worker.box_counter - 1)) if self.boxes_worker.box_counter > 0 else self.ui.CurrentBoxOnPalletLabel.setText(str(0))



        new_pack_number = int(self.current_pack_number) + 1
        self.current_pack_number = f'{new_pack_number:012d}'
        self.add_db_pack(self.current_pack_number, weight_netto, weight_brutto)
        self.pack_counter += 1

        logger.debug(f'box counter = {self.boxes_worker.box_counter}')
        logger.debug(f'pack counter = {self.pack_counter}')

        if self.pack_counter == self.boxes_worker.pack_in_box:
            logger.debug(f'Condition of close box success.')
            self.close_box()

        if self.boxes_worker.box_status == 'Closed':
            self.complete_adding_pack.emit()

    def add_db_pack(self, number_pack: str, weight_netto: float, weight_brutto: float):
        with get_db_session() as db:
            box_id = db.query(Boxes).filter(Boxes.number == self.boxes_worker.current_box_number).first()
            pack_row = Pack(
                number=number_pack,
                created_at=datetime.now(),
                box_id=box_id.id,
                nomenclature_id=self.boxes_worker.get_current_nomenclature().id,
                weight_netto=weight_netto,
                weight_brutto=weight_brutto,
                status='Created'

            )
            db.add(pack_row)
            db.commit()

    def close_box(self):
        logger.debug(f'pack counter: {self.pack_counter}')
        if self.pack_counter == 0:
            self.boxes_worker.show_error_window(1)
        else:
            self.pack_counter = 0
            self.boxes_worker.change_close_box_status(self.boxes_worker.current_box_number)
            QTimer.singleShot(0, lambda: self.complete_adding_pack.emit())

            if self.boxes_worker.box_counter == self.boxes_worker.pack_in_box:
                logger.debug(f'Condition of close pallet success.')
                self.boxes_worker.close_pallet()

            if self.boxes_worker.pallet_worker.pallet_status == 'Closed':
                self.boxes_worker.complete_adding_pallet.emit()

    @Slot()
    def complete_add_pack(self):
        self.closer_box.emit(self.boxes_worker.current_box_number)
        self.ui.stackedWidget_3.setCurrentIndex(1)

    def cancel_pack(self):
        new_pack_number = int(self.current_pack_number) - 1
        self.current_pack_number = f'{new_pack_number:012d}'

    @staticmethod
    def get_twenty_last_pack():
        with get_db_session() as db:
            las_twenty_pack = db.query(Pack).options(joinedload(Pack.nomenclature),
                                                     joinedload(Pack.boxes).joinedload(Boxes.pallet)).order_by(
                Pack.id.desc()).limit(20).all()
            return las_twenty_pack
