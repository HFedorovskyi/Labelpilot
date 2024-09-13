# database_setup.py
from sqlalchemy.orm import Session
from datebase.datebase_main import SessionLocal, Base, engine, Nomenclature, Container, User

def create_test_data():
    # Создание сессии
    db = SessionLocal()

    # Создание контейнеров
    container1 = Container(name='Small Box', weight=0.5)
    container2 = Container(name='Medium Box', weight=1.0)
    db.add(container1)
    db.add(container2)
    db.commit()

    # Создание номенклатуры
    nomenclature1 = Nomenclature(
        name='Product 1',
        article='001',
        exp_date=30,
        portion_container=container1,
        box_container=container2,
        close_box_counter=6,
        close_pallet_counter=30,
    )
    nomenclature2 = Nomenclature(
        name='Product 2',
        article='002',
        exp_date=60,
        portion_container=container1,
        box_container=container2,
        close_box_counter=6,
        close_pallet_counter=30,
    )
    db.add(nomenclature1)
    db.add(nomenclature2)
    db.commit()



    # Закрытие сессии
    db.close()

if __name__ == "__main__":
    create_test_data()
