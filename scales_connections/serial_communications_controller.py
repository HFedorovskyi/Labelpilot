from PySide6.QtWidgets import QMessageBox
from scales_connections.serial_communication import SerialWorker
from scales_connections.base_controller import BaseScaleController
import scales_connections.scale_protocols as protocols
from PySide6.QtCore import Slot


class SerialController(BaseScaleController):
    '''Отображение данных связанных с подключение по COM и создание экземпляра коммуникатора с весами.'''

    def __init__(self, ui):
        super().__init__(ui)
        self.protocol = protocols.PROTOCOLS_SERIAL.get(
            ui.ListScalecomboBox_2.currentText())
        self.ui.checkConnectionScaleBtn.clicked.connect(self.check_connection)
        self.ui.ListScalecomboBox_2.currentIndexChanged.connect(self.change_serial_protocols)

    def setup_connector(self):  #Создаём экземпляр SerialWorker, устанавливаем вывод информации и запускаем считывание
        self.connector = SerialWorker(self.ui.ChoseComPortcomboBox.currentText(), self.protocol)
        if self.connector.is_connected(self.ui.ChoseComPortcomboBox.currentText()):
            self.connector.data_received.connect(self.on_data_received)
            self.connector.start()
        else:
            QMessageBox.critical(self.ui, "Ошибка соединения", "Failed to connect to the selected COM port")

    def check_connection(self):  #проверка подключения к COM
        port = self.ui.ChoseComPortcomboBox.currentText()
        protocol = self.ui.ListScalecomboBox.currentText()
        connector = SerialWorker(port, protocol)
        result = connector.is_connected(self.ui.ChoseComPortcomboBox.currentText())
        self.ui.label_47.setText(str(result))

    @Slot()
    def change_serial_protocols(self):
        self.protocol = protocols.PROTOCOLS_SERIAL.get(
            self.ui.ListScalecomboBox_2.currentText())
        print(self.protocol)
