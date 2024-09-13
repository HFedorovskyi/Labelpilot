import os
import sys
from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, JSON, String, Float, ForeignKey, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

if getattr(sys, 'frozen', False):
    # Если приложение запущено в режиме "frozen" (скомпилировано)
    main_directory_path = os.path.dirname(sys.executable)
    application_path = os.path.join(main_directory_path, 'datebase', )

else:
    # Если приложение запущено в режиме разработки
    application_path = os.path.dirname(__file__)

database_path = os.path.join(application_path, 'client_data.db')
DATABASE_URL = f"sqlite:///{database_path}"

# Создаем путь к базе данных в папке 'database'


engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Nomenclature(Base):
    __tablename__ = 'nomenclature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    article = Column(String, nullable=True)
    exp_date = Column(Integer, nullable=False)
    portion_container_id = Column(Integer, ForeignKey('container.id'), nullable=True)
    box_container_id = Column(Integer, ForeignKey('container.id'), nullable=True)
    labels_id = Column(Integer, ForeignKey('labels.id'), nullable=True)
    close_box_counter = Column(Integer, nullable=True)
    portion_container = relationship("Container", foreign_keys=[portion_container_id])
    box_container = relationship("Container", foreign_keys=[box_container_id])
    pack = relationship("Pack", back_populates="nomenclature", cascade='all, delete-orphan')
    labels = relationship("Labels", backref="nomenclatures")

class Container(Base):
    __tablename__ = 'container'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Pallet(Base):
    __tablename__ = 'pallet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    status = Column(String, nullable=False, default='Open')
    weight = Column(Float, nullable=True)

    boxes = relationship("Boxes", back_populates="pallet", cascade='all, delete-orphan')


class Boxes(Base):
    __tablename__ = 'boxes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pallete_id = Column(Integer, ForeignKey('pallet.id'), nullable=False)
    number = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=None)
    status = Column(String, nullable=False, default='Open')

    pallet = relationship("Pallet", back_populates="boxes")
    pack = relationship("Pack", back_populates="boxes", cascade='all, delete-orphan')


class Pack(Base):
    __tablename__ = 'pack'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.now)
    box_id = Column(Integer, ForeignKey('boxes.id'), nullable=False)
    nomenclature_id = Column(Integer, ForeignKey('nomenclature.id'), nullable=False)
    weight_netto = Column(Float, nullable=False)
    weight_brutto = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    boxes = relationship("Boxes", back_populates="pack")
    nomenclature = relationship("Nomenclature", back_populates="pack")



class UUID(Base):
    __tablename__ = 'uuid'

    uuid_client = Column(String, nullable=False, primary_key=True)


class Barcodes(Base):
    __tablename__ = 'barcodes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type_barcodes = Column(String, nullable=False, unique=True)
    structure = Column(JSON, nullable=False, unique=True)
    additional_info = Column(JSON, nullable=False, unique=True)


class Labels(Base):
    __tablename__ = 'labels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    structure = Column(JSON, nullable=False, unique=True)



def update_model_from_table(engine, table_name, model_class):
    """
    Обновляет модель SQLAlchemy на основе колонок в таблице базы данных.
    """
    # Получаем инспектор
    inspector = inspect(engine)

    # Получаем текущие колонки таблицы
    columns_in_db = inspector.get_columns(table_name)
    existing_columns = {column.name for column in model_class.__table__.columns}

    # Добавляем отсутствующие колонки в класс модели
    for column_info in columns_in_db:
        col_name = column_info['name']
        if col_name not in existing_columns:
            # Добавляем новый атрибут-колонку в класс модели
            setattr(model_class, col_name, Column(col_name, String))
            print(f"Добавлена колонка '{col_name}' в класс {model_class.__name__}.")



Base.metadata.create_all(engine)


update_model_from_table(engine, 'nomenclature', Nomenclature)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
