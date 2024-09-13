from alembic import command
from sqlalchemy import String, Column, inspect, text
from datebase.datebase_main import engine, Nomenclature, update_model_from_table
import os
import sys
from alembic.config import Config


class AutoMigrateDB:
    def __init__(self):
        self.engine = engine
        self.prohibited_columns = {'id', "name", "article", "exp_date", 'close_box_counter', 'portion_container_id',
                                 'box_container_id', 'created', 'edited', 'labels_id'}# Используем ваш настроенный движок базы данных

        if getattr(sys, 'frozen', False):
            # Если приложение запущено в режиме "frozen" (скомпилировано)
            main_directory_path = os.path.dirname(sys.executable)
            application_path = os.path.join(main_directory_path, 'datebase')
        else:
            # Если приложение запущено в режиме разработки
            application_path = os.path.dirname(__file__)

        # Используем динамический путь для файла alembic.ini
        self.alembic_cfg = Config(os.path.join(application_path, '..', 'alembic.ini'))
        self.alembic_cfg.set_main_option("script_location", os.path.join(application_path, '..', 'alembic'))

    def autogenerate_migration(self, message):
        """
        Автоматически создает миграцию на основе текущей схемы базы данных.
        """
        try:
            command.revision(self.alembic_cfg, message=message, autogenerate=True)
            print("Автоматическая миграция создана.")
        except Exception as e:
            print(f"Ошибка при создании миграции: {e}")

    def upgrade_db(self):
        """
        Применяет последнюю миграцию к базе данных.
        """
        command.upgrade(self.alembic_cfg, 'head')
        update_model_from_table(self.engine, 'nomenclature', Nomenclature)
        print("База данных успешно обновлена до последней версии.")

    def update_database_structure(self, schema_data):
        """
        Сравнивает текущую структуру базы данных с новой схемой и автоматически создает миграцию.
        """
        table_name, new_columns = self.convert_schema_data_to_sqlalchemy_format(schema_data)
        if self.need_migration(table_name, new_columns):
            # Применяем изменения к базе данных
            self.apply_new_columns_to_database(table_name, new_columns)
            # Теперь создаем миграцию
            self.autogenerate_migration("Automatic migration based on schema update")
            # Применяем миграцию
            self.upgrade_db()
        else:
            print("Миграция не требуется. Структура таблицы актуальна.")

    def need_migration(self, table_name, new_columns):
        """
        Проверяет, нужно ли создавать миграцию.
        Сравнивает текущую структуру базы данных с новой схемой.
        """
        # Получаем текущую структуру таблицы
        inspector = inspect(self.engine)
        existing_columns = inspector.get_columns(table_name)

        # Преобразуем текущую структуру в удобный для сравнения формат
        existing_column_names = {col['name'] for col in existing_columns if col['name'] not in self.prohibited_columns}

        # Определяем, нужно ли добавлять новые колонки или удалять старые
        new_column_names = set(new_columns.keys())
        if new_column_names != existing_column_names:
            print("Изменения в структуре таблицы обнаружены.")
            return True
        else:
            print("Изменений в структуре таблицы не обнаружено.")
            return False

    def apply_new_columns_to_database(self, table_name, new_columns):
        """
        Применяет новые колонки к базе данных и удаляет отсутствующие.
        """
        with self.engine.connect() as connection:
            # Получаем текущую структуру таблицы
            inspector = inspect(self.engine)
            existing_columns = {col['name'] for col in inspector.get_columns(table_name)}

            # Определяем колонки для удаления
            columns_to_remove = existing_columns - set(new_columns.keys())

            columns_to_remove = columns_to_remove - self.prohibited_columns

            # Удаляем колонки
            for col_name in columns_to_remove:
                print(f"Удаление колонки {col_name} из таблицы {table_name}")
                connection.execute(text(f"ALTER TABLE {table_name} DROP COLUMN \"{col_name}\""))

            # Добавляем новые колонки
            for col_name, column in new_columns.items():
                if col_name not in existing_columns:
                    print(f"Добавление колонки {col_name} в таблицу {table_name}")
                    connection.execute(text(f"ALTER TABLE {table_name} ADD COLUMN \"{col_name}\" TEXT"))

    def convert_schema_data_to_sqlalchemy_format(self, schema_data):
        """
        Преобразует данные схемы из формата JSON в формат SQLAlchemy.
        """
        table_name = "nomenclature"  # Название таблицы
        sqlalchemy_columns = {}
        forbidded_columns = {"name", "article", "exp_date", 'close_box_counter', 'portion_container_id',
                             'box_container_id', 'created', 'edited', 'labels_id'}
        for column in schema_data:
            if isinstance(column, dict) and column['name'] not in forbidded_columns:
                column_name = column['name']
                sqlalchemy_column = Column(column_name, String, nullable=True)
                sqlalchemy_columns[column_name] = sqlalchemy_column
            else:
                print(f"Колонка '{column['name']}' не будет изменена.")
        print(sqlalchemy_columns)
        return table_name, sqlalchemy_columns
