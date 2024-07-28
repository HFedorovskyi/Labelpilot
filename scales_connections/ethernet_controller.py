from PySide6.QtWidgets import QMessageBox
from scales_connections.ethernet_communication import EthernetWorker
from scales_connections.base_controller import BaseScaleController
from PySide6.QtCore import Signal, Slot, QThread, QObject
import socket
import time
import scales_connections.scale_protocols as protocols


class ConnectionChecker(QObject):
    '''Проверка подключения к адресу и порту, которые указааны в настройках.'''
    progress_updated = Signal(int)
    connection_result = Signal(str)

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port

    def check_connection(self):
        progress = 0
        self.progress_updated.emit(progress)


        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Разделение задачи на части для демонстрации прогресса
            steps = 10
            for i in range(steps):
                time.sleep(0.1)  # Искусственная задержка для демонстрации
                progress += 10
                self.progress_updated.emit(progress)

            sock.connect((self.ip, self.port))
            sock.close()
            self.connection_result.emit(f'Successfully connected to {self.ip}:{self.port}')
        except (socket.timeout, socket.error) as e:
            self.connection_result.emit(str(e))
        finally:
            self.progress_updated.emit(100)


class EthernetController(BaseScaleController):
    '''Отображение данных связаных с подключение по Ethernet и создание коммуникатора с весами. Так же опрееделена функция
    для отображения статус бара проверки подключения. Класс наследуется от базового класса
    для контроллеров.'''
    progress_updated = Signal(int)
    connection_result = Signal(str)

    def __init__(self, ui):
        super().__init__(ui)
        self.protocol = protocols.PROTOCOLS_ETHERNET.get(self.ui.ListScalecomboBox.currentText())
        self.sock = None
        self.ip_adress = None
        self.port = None
        self.ui.checkConnectionScaleNetworkBtn_2.clicked.connect(self.check_connection)
        self.connector = None
        self.progress_updated.connect(self.update_progress_bar)

    def setup_connector(self):
        self.ip_adress = self.ui.setIPlineEdit.text()
        self.port = int(self.ui.setNetworkPortlineEdit.text())   #### Перевожу в int для Nuitka
        self.connector = EthernetWorker(self.ip_adress, self.port, self.protocol)
        if self.connector.is_connected(self.ip_adress, self.port):
            self.connector.data_received.connect(self.on_data_received)

        else:
            QMessageBox.critical(self.ui, "Ошибка соединения", "Failed to connect to the selected IP and port")

    def check_connection(self):
        self.ui.centralwidget.setEnabled(False)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setVisible(True)

        self.ip_address = self.ui.setIPlineEdit.text()
        self.port = int(self.ui.setNetworkPortlineEdit.text()) if self.ui.setNetworkPortlineEdit.text() else None
        if self.ip_address != '...' and self.port:
            print(f'{self.ip_address}:{self.port}')
            self.connection_checker = ConnectionChecker(self.ip_address, self.port)
            self.connection_thread = QThread()

            self.connection_checker.moveToThread(self.connection_thread)
            self.connection_thread.started.connect(self.connection_checker.check_connection)

            self.connection_checker.progress_updated.connect(self.update_progress_bar)
            self.connection_checker.connection_result.connect(self.on_connection_result)

            self.connection_thread.start()
        else:
            self.ui.progressBar.setVisible(False)
            self.ui.centralwidget.setEnabled(True)
            self.ui.label_20.setText(f'Некорректные параметры ввода')



    @Slot(str)
    def on_connection_result(self, result):
        self.ui.label_35.setText(result)
        self.connection_thread.quit()
        self.connection_thread.wait()
        self.ui.progressBar.setVisible(False)
        self.ui.centralwidget.setEnabled(True)

    @Slot(int)
    def update_progress_bar(self, value):
        self.ui.progressBar.setValue(value)

    def closeEvent(self, event):  # Действия при закрытии окна
        if self.connector:
            self.connector.stop()
        event.accept()
