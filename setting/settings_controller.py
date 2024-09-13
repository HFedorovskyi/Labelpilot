import json
import os
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QObject, Slot
from scales_connections.serial_communication import SerialWorker
from print_label.print_label_func import get_printers
from scales_connections.scale_protocols import PROTOCOLS_SERIAL, PROTOCOLS_ETHERNET
import sys


class SaveLoadSettingsManager:
    def __init__(self, file='settings.json'):
        if getattr(sys, 'frozen', False):
            # Если приложение запущено в режиме "frozen" (скомпилировано)
            base_path = os.path.dirname(sys.executable)
        else:
            # Если приложение запущено в режиме разработки
            base_path = os.path.dirname(__file__)
        # Определяем путь к директории исполняемого файла
        self.file = os.path.join(base_path, file)

    def load_settings(self):
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self, settings):
        with open(self.file, 'w') as f:
            json.dump(settings, f, indent=4)


class SettingsController(QObject):

    def __init__(self, ui, main_window):
        super().__init__()
        self.settings_manager = SaveLoadSettingsManager()
        self.ui = ui
        self.main_window = main_window
        self.ui.ListScalecomboBox_2.addItems(PROTOCOLS_SERIAL.keys())
        self.ui.ListScalecomboBox.addItems(PROTOCOLS_ETHERNET.keys())
        self.ui.saveSetting.clicked.connect(self.save_settings)
        self.ui.saveSetting_2.clicked.connect(self.save_settings)
        self.ui.choseScaleConnectButtnGroup.idToggled.connect(self.change_choseConnectioncomboBox)
        self.ui.progressBar.setVisible(False)

    def save_settings(self):  # Сохранения настроек
        settings = {
            'connection_type': self.ui.choseScaleConnectButtnGroup.checkedId(),
            'selected_port': self.ui.ChoseComPortcomboBox.currentText(),
            'print_if_weight_stable': self.ui.checkBoxWeightStablity.isChecked(),
            'portions_printer': self.ui.chosePrinterPortionLabelComboBox.currentText(),
            'sum_printer': self.ui.chosePrinterSumLabelComboBox.currentText(),
            'pallet_printer': self.ui.chosePrinterSPalLabelComboBox.currentText(),
            'scale': self.ui.ListScalecomboBox_2.currentIndex(),
            'ip': self.ui.setIPlineEdit.text(),
            'port': self.ui.setNetworkPortlineEdit.text(),
            'show_batch': self.ui.checkBoxBatchUse.isChecked(),
            'protocol_ethernet': self.ui.ListScalecomboBox.currentIndex(),
            'protocol_com': self.ui.ListScalecomboBox_2.currentIndex(),

            'max_box_on_pallet': self.ui.MaxBoxOnPalletLineEdit.text(),

        }
        self.settings_manager.save_settings(settings)
        QMessageBox.information(self.main_window, "Сохранение настроек", "Сохранено")

    def load_settings(self):
        # Загрузка настроек
        settings = self.settings_manager.load_settings()
        selected_port = settings.get('selected_port', "")
        selected_printer_portion = settings.get('portions_printer', "")
        selected_sum_portion = settings.get('sum_printer', "")
        pallet_printer = settings.get('pallet_printer', "")
        scale = settings.get('scale', 0)
        ip = settings.get('ip', "")
        network_port = settings.get('port', '12345')
        connection_type = settings.get('connection_type', -4)
        show_batch = settings.get('show_batch', False)
        protocol_ethernet = settings.get('protocol_ethernet', 0)
        protocol_com = settings.get('protocol_com', 0)
        max_box_on_pallet = settings.get('max_box_on_pallet', 0)

        self.ui.ListScalecomboBox_2.setCurrentIndex(int(scale))
        self.ui.choseScaleConnectButtnGroup.button(connection_type).setChecked(True)
        self.ui.checkBoxWeightStablity.setChecked(settings.get('print_if_weight_stable', False))
        self.ui.setIPlineEdit.setText(ip)
        self.ui.setNetworkPortlineEdit.setText(network_port)
        self.change_choseConnectioncomboBox(connection_type)
        self.ui.checkBoxBatchUse.setChecked(show_batch)
        self.ui.ListScalecomboBox.setCurrentIndex(protocol_ethernet)
        self.ui.ListScalecomboBox_2.setCurrentIndex(protocol_com)
        self.ui.MaxBoxOnPalletLineEdit.setText(str(max_box_on_pallet))
        self.show_batch()

        ports = SerialWorker.get_ports()
        printers = get_printers()

        # Очистка комбобоксов
        self.ui.ChoseComPortcomboBox.clear()
        self.ui.chosePrinterPortionLabelComboBox.clear()
        self.ui.chosePrinterSPalLabelComboBox.clear()
        self.ui.chosePrinterSumLabelComboBox.clear()

        # Заполнение комбобоксов с портами
        for port in ports:
            self.ui.ChoseComPortcomboBox.addItem(port)
        if selected_port in ports:
            self.ui.ChoseComPortcomboBox.setCurrentText(selected_port)

        # Заполнение комбобоксов с принтерами
        for printer in printers:
            printer_name = printer['pPrinterName']
            self.ui.chosePrinterPortionLabelComboBox.addItem(printer_name)
            self.ui.chosePrinterSPalLabelComboBox.addItem(printer_name)
            self.ui.chosePrinterSumLabelComboBox.addItem(printer_name)

        # Установка текущего текста для принтеров
        if selected_printer_portion in [printer['pPrinterName'] for printer in printers]:
            self.ui.chosePrinterPortionLabelComboBox.setCurrentText(selected_printer_portion)
        if selected_sum_portion in [printer['pPrinterName'] for printer in printers]:
            self.ui.chosePrinterSumLabelComboBox.setCurrentText(selected_sum_portion)
        if pallet_printer in [printer['pPrinterName'] for printer in printers]:
            self.ui.chosePrinterSPalLabelComboBox.setCurrentText(pallet_printer)

    @Slot(int)
    def change_choseConnectioncomboBox(self, index):
        if index == -4:
            self.ui.stackedWidget_2.setCurrentIndex(0)
        elif index == -3:
            self.ui.stackedWidget_2.setCurrentIndex(1)

    def show_batch(self):
        if self.ui.checkBoxBatchUse.isChecked():
            self.ui.batchNumberlineEdit.show()
            self.ui.label_11.show()
        else:
            self.ui.batchNumberlineEdit.hide()
            self.ui.label_11.hide()
