import socket
from PySide6.QtCore import QTimer
import json
import threading
import requests
from http.server import BaseHTTPRequestHandler
from datebase.create_uuid import ger_or_create_uuid
from datebase.update_DB import AutoMigrateDB
from datebase.datebase_main import Nomenclature, get_db_session, Barcodes


class StatusSender:

    UUID = ger_or_create_uuid()
    SERVER_URL = 'http://127.0.0.1:8000/label_stations/check_status/'

    def __init__(self, interval=300000):
        self.interval = interval  # Интервал в миллисекундах (по умолчанию 5 минут)
        self.timer = QTimer()  # QTimer для периодической отправки
        self.timer.timeout.connect(self.send_status_to_server)  # Подключение функции отправки к таймеру
        self.timer.start(self.interval)  # Запуск таймера

    def send_status_to_server(self):
        """
        Метод для отправки статуса станции на сервер.
        """
        threading.Thread(target=self._send_status_thread).start()

    def _send_status_thread(self):
        """
        Фоновая задача для выполнения HTTP-запроса.
        """

        print('start statussender')
        ip_address = self.get_current_ip()
        try:
            response = requests.post(self.SERVER_URL, json={'uuid': self.UUID, 'ip': ip_address})
            if response.status_code == 200:
                print("Статус успешно обновлен на сервере.")
            else:
                print(f"Ошибка при обновлении статуса: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при подключении к серверу: {e}")

    def get_current_ip(self):
        """
        Получение текущего IP-адреса станции.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


class ConnectionsWithServer(BaseHTTPRequestHandler):

    UUID = ger_or_create_uuid()
    updater_db = AutoMigrateDB()
    db_controller = None


    def do_GET(self):
        """
        Обработка GET-запроса для проверки статуса станции.
        """
        if self.path == '/check-status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'hostname': socket.gethostname(),
                'uuid': self.UUID,  # Подставьте ваш UUID станции
                'status': 'online',
                'ip_address': self.client_address[0],
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """
        Обработка POST-запроса для получения номенклатуры или других данных.
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        data = json.loads(post_data.decode('utf-8'))

        if 'nomenclatures' in data:
            try:
                self.updater_db.update_database_structure(data['nomenclatures_field'])
                self.update_nomenclature_data(data['nomenclatures'])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"status": "error", "message": "' + str(e).encode('utf-8') + b'"}')

        elif 'barcodes' in data:
            try:
                self.update_barcodes_data(data['barcodes'])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"status": "error", "message": "' + str(e).encode('utf-8') + b'"}')



    def update_nomenclature_data(self, server_data):
        # Ключи, которые нужно удалить из словаря
        keys_to_remove = ['order', 'created', 'edited']

        # Преобразуем данные сервера: удаляем ненужные ключи и преобразуем значение id
        processed_data = []
        for item in server_data:
            # Удаляем ненужные ключи
            for key in keys_to_remove:
                item.pop(key, None)  # Используем pop с default значением None чтобы избежать ошибки если ключа нет

            # Обрабатываем поля portion_container_id и box_container_id
            if 'portion_container_id' in item and isinstance(item['portion_container_id'], list) and item[
                'portion_container_id']:
                item['portion_container_id'] = item['portion_container_id'][0]['id']
            else:
                item['portion_container_id'] = None

            if 'box_container_id' in item and isinstance(item['box_container_id'], list) and item['box_container_id']:
                item['box_container_id'] = item['box_container_id'][0]['id']
            else:
                item['box_container_id'] = None

            # Добавляем обработанный элемент в новый список
            processed_data.append(item)

        with get_db_session() as session:
            # Получаем все текущие строки в таблице 'Nomenclature' на клиенте
            current_rows = session.query(Nomenclature).all()

            # Преобразуем текущие строки в словарь для быстрого доступа по id
            current_data_dict = {row.id: row for row in current_rows}
            # Обработка обновлений и добавлений
            for server_item in processed_data:
                server_id = server_item['id']
                if server_id in current_data_dict:
                    # Если строка существует, обновляем её
                    row = current_data_dict[server_id]
                    for key, value in server_item.items():
                        if hasattr(row, key):
                            setattr(row, key, value)
                else:
                    new_row = Nomenclature(**server_item)
                    session.add(new_row)


            # Удаление строк, которых нет в данных сервера
            server_ids = {item['id'] for item in processed_data}
            for client_id in list(current_data_dict.keys()):
                if client_id not in server_ids:
                    session.delete(current_data_dict[client_id])

            # Сохранение всех изменений в базе данных
            session.commit()

        self.update_combobox()
        print("Данные в таблице 'Nomenclature' успешно обновлены.")

    def update_combobox(self):
        # Получаем текущие значения из комбобокса и превращаем их в множество
        current_values = [self.db_controller.ui.NomenclatureComboBox.itemText(i)
                          for i in range(self.db_controller.ui.NomenclatureComboBox.count())]
        current_values_set = set(current_values)

        # Получаем значения из базы данных и превращаем их в множество
        db_values = self.db_controller.get_all_nomenclatures()  # Предполагаем, что этот метод возвращает список значений из базы данных
        db_values_set = set(db_values)

        # Находим значения, которые нужно добавить и удалить
        values_to_add = db_values_set - current_values_set
        values_to_remove = current_values_set - db_values_set

        # Добавляем отсутствующие значения в комбобокс
        for value in values_to_add:
            self.db_controller.ui.NomenclatureComboBox.addItem(value)

        # Удаляем лишние значения из комбобокса
        for value in values_to_remove:
            index = self.db_controller.ui.NomenclatureComboBox.findText(value)
            if index != -1:  # Проверяем, найден ли элемент в комбобоксе
                self.db_controller.ui.NomenclatureComboBox.removeItem(index)

        # Сохраняем текущее выбранное значение, если оно все еще присутствует в новом наборе данных
        current_value = self.db_controller.ui.NomenclatureComboBox.currentText()
        if current_value in db_values_set:
            self.db_controller.ui.NomenclatureComboBox.setCurrentText(current_value)
        else:
            print("Сохраненное значение отсутствует в новом наборе данных.")


    def update_barcodes_data(self, server_data):
        keys_to_remove = ['order', 'Created on', 'Last modified']

        # Преобразуем данные сервера: удаляем ненужные ключи и преобразуем значение id
        for item in server_data:
            # Удаляем ненужные ключи
            for key in keys_to_remove:
                item.pop(key, None)  # Используем pop с default значени

        with get_db_session() as session:
            # Получаем все текущие строки в таблице 'Nomenclature' на клиенте
            current_rows = session.query(Barcodes).all()


            # Преобразуем текущие строки в словарь для быстрого доступа по id
            current_data_dict = {row.id: row for row in current_rows}
            # Обработка обновлений и добавлений
            for server_item in server_data:
                server_id = server_item['id']
                if server_id in current_data_dict:
                    # Если строка существует, обновляем её
                    row = current_data_dict[server_id]
                    for key, value in server_item.items():
                        if hasattr(row, key):
                            setattr(row, key, value)
                else:
                    try:
                        new_row = Barcodes(**server_item)
                        session.add(new_row)
                    except Exception as e:
                        print(e)



            # Удаление строк, которых нет в данных сервера
            server_ids = {item['id'] for item in server_data}
            for client_id in list(current_data_dict.keys()):
                if client_id not in server_ids:
                    session.delete(current_data_dict[client_id])

            # Сохранение всех изменений в базе данных
            session.commit()

        self.update_combobox()
        print("Данные в таблице 'Barcodes' успешно обновлены.")

