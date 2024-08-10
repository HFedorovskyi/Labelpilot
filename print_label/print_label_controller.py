from PySide6.QtCore import QObject, Slot
from print_label.print_label_func import PrintWorker
import threading


class PrintLabelController(QObject):

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.print_worker = None
        self.print_thread = None
        self.is_printed = False

    @Slot()
    def print_label(self, weight):  #Печать этикетки
        current_nomenclature = self.ui.NomenclatureComboBox.currentText()
        self.start_print_thread(weight, current_nomenclature)

        self.is_printed = True

    def start_print_thread(self,
                           weight,
                           current_nomenclature):  # Запуск потока печати этикетки, возможно поток уберём, посмотрим разницу в скорости
        self.print_worker = PrintWorker(weight, current_nomenclature, self.ui)
        self.print_thread = threading.Thread(target=self.print_worker.run)
        self.print_thread.start()
