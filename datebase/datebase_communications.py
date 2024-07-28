from datebase.datebase_main import get_db_session
from datebase.datebase_main import Nomenclature, Pallet, Boxes, Pack
from datetime import datetime


class WorkWithPallet:

    def __init__(self):
        self.current_pallet = self.get_last_pallet_number().number
        self.max_box_on_pallet = 5

    def generate_pallet_number(self, last_pallet_number):
        date_now = datetime.now()
        formated_date = date_now.strftime("%d%m%Y")
        new_pallet_number = f'46{formated_date}{(int(last_pallet_number[10:]) + 1):007d}'
        self.add_db_new_pallet(new_pallet_number)
        self.current_pallet = new_pallet_number
        return new_pallet_number

    @staticmethod
    def new_pallet_number():
        date_now = datetime.now()
        formated_date = date_now.strftime("%d%m%Y")
        return f'46{formated_date}00000000'

    def get_last_pallet_number(self):
        with get_db_session() as db:
            last_pallet = db.query(Pallet.number).order_by(Pallet.id.desc()).limit(1).first()
            if last_pallet:
                return last_pallet
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


class WorkWithBoxes:

    def __init__(self, ui):
        self.ui = ui
        self.box_counter = 0
        self.current_box_number = self.last_box()
        self.pallet_worker = WorkWithPallet()
        self.pack_in_box = self.get_current_nomenclature().close_box_counter

    def new_box(self):
        last_box_number = self.current_box_number
        self.change_close_box_status(last_box_number)
        new_box_number = int(last_box_number) + 1
        self.add_db_new_box(f'{new_box_number:012d}')
        self.box_counter += 1
        if self.box_counter == self.pallet_worker.max_box_on_pallet:
            self.pallet_worker.generate_pallet_number(self.pallet_worker.current_pallet)
            self.box_counter = 0
        self.current_box_number = f'{new_box_number:012d}'
        return f'{new_box_number:012d}'

    def last_box(self):
        with get_db_session() as db:
            last_box_number = db.query(Boxes).order_by(Boxes.id.desc()).limit(1).first()
            if last_box_number:
                return last_box_number.number
            else:
                self.add_db_new_box(f'{0:012d}')
                return f'{0:012d}'

    @staticmethod
    def change_close_box_status(box_number):
        with get_db_session() as db:
            print(box_number)
            change_box = db.query(Boxes).filter(Boxes.number == box_number).first()
            print(change_box)
            change_box.status = 'Closed'
            change_box.updated_at = datetime.now()

            db.commit()

    @staticmethod
    def add_db_new_box(box_number):
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


class WorkWithPack:

    def __init__(self, ui):
        self.ui = ui
        self.boxes_worker = WorkWithBoxes(self.ui)
        self.current_pack_number = self.get_last_pack_number()
        self.pack_counter = 0


    def get_last_pack_number(self):
        with get_db_session() as db:
            last_pack_number = db.query(Pack).order_by(Pack.id.desc()).limit(1).first()
            if last_pack_number:
                return last_pack_number.number
            else:
                return f'{0:012d}'

    def new_pack_number(self, weight_netto, weight_brutto):
        new_pack_number = int(self.current_pack_number) + 1
        self.current_pack_number = f'{new_pack_number:012d}'
        self.add_db_pack(self.current_pack_number, weight_netto, weight_brutto)

    def add_db_pack(self, number_pack, weight_netto, weight_brutto):
        with get_db_session() as db:
            pack_row = Pack(
                number=number_pack,
                created_at=datetime.now(),
                box_id=self.boxes_worker.current_box_number,
                nomenclature_id=self.boxes_worker.get_current_nomenclature().id,
                weight_netto=weight_netto,
                weight_brutto=weight_brutto,
                status='Created'

            )
            db.add(pack_row)
            db.commit()
            self.pack_counter += 1
            if self.pack_counter == self.boxes_worker.pack_in_box:
                self.boxes_worker.new_box()
                self.pack_counter = 0
