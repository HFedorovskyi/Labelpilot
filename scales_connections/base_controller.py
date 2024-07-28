from PySide6.QtCore import QObject, Signal, Slot, QTimer
from print_label.print_label_controller import PrintLabelController
from collections import deque
import abc
from abc import ABCMeta
from datebase.datebase_controller import FillTreeWidgetDbController


class QObjectMeta(ABCMeta, type(QObject)):
    pass


class BaseScaleController(QObject, abc.ABC, metaclass=QObjectMeta):
    '''Родительский класс для получения данных с весово и отображения в интерфейсе.
    Так же здесб прописана логика печати по стабилизации веса'''
    data_received = Signal(float)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.connector = None
        self.fillTreeWidget = FillTreeWidgetDbController(self.ui)
        self.current_weight = 0
        self.previous_weights = deque(maxlen=3)  # Хранение последних 3 значений веса
        self.stability_threshold = 3  #Определение стабильности - 3 раза подряд сигнал с одинаковым весом - вес стабилен# устанавливем протокол для выбраных весов в настройках
        self.ui.indicationWeightBruttoBrowser.setText('0.00')
        self.ui.indicationWeightNettotextBrowser.setText('0.00')
        self.weight_stable_timer = QTimer()
        self.print_controller = PrintLabelController(ui)
        self.ui.printPortionBtn.clicked.connect(self.print_label_without_stability)


    @abc.abstractmethod
    def setup_connector(self):
        "Создания обьекта подключения"

    def start(self):
        if self.connector:
            self.connector.start()

    def stop(self):
        if self.connector:
            self.connector.stop()

    @abc.abstractmethod
    def check_connection(self):
        'Проверка подключения'

    @Slot(str)
    def on_data_received(self, data):  #Слот для вывода данных с коннектора

        self.previous_weights.append(self.current_weight)
        self.current_weight = data
        if self.current_weight == 0:
            self.ui.widget_5.setStyleSheet(' border-radius: 10px;border: 1px solid gray;')
        self.ui.indicationWeightBruttoBrowser.setText(f'{data}')
        self.ui.indicationWeightNettotextBrowser.setText(
            f'{data - float(self.ui.conteinerWeightTextBrowser.toPlainText())}')

    def check_weight_stability(self):#Проверка стабильности веса и печать по стабилизации
        if len(self.previous_weights) == self.stability_threshold and all(
                w == self.current_weight for w in self.previous_weights):
            if not self.print_controller.is_printed:
                self.ui.widget_5.setStyleSheet(
                    'border-radius: 10px;border: 1px solid gray;background-color: rgb(167, 255, 157)')
                self.print_controller.print_label(self.current_weight)
                self.fillTreeWidget.write_to_ContainerstreeWidget(self.ui.indicationWeightNettotextBrowser.toPlainText(),
                                    self.ui.indicationWeightBruttoBrowser.toPlainText())
        else:
            if self.current_weight == 0:
                self.ui.widget_5.setStyleSheet('border-radius: 10px;border: 1px solid gray;')
            else:
                self.ui.widget_5.setStyleSheet(
                    'border-radius: 10px;border: 1px solid gray;background-color: rgb(255, 88, 66)')
            self.print_controller.is_printed = False

    def set_weight_stable_timer(self):
        if self.ui.checkBoxWeightStablity.isChecked():
            self.weight_stable_timer.timeout.connect(self.check_weight_stability)
            self.weight_stable_timer.start(50)
        else:
            self.weight_stable_timer.stop()

    def print_label_without_stability(self):
        self.print_controller.print_label(self.current_weight)

    def closeEvent(self, event):  # Действия при закрытии окна
        self.connector.stop()
        self.weight_stable_timer.stop()
        event.accept()
