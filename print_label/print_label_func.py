from PySide6.QtCore import QObject, Signal
from print_label.label_gen import LabelGenerator
import win32print


class PrintWorker(QObject):
    finished = Signal()

    def __init__(self, weight, current_nomenclature, ui):
        super().__init__()
        self.ui = ui
        self.weight = weight
        self.current_nomenclature = current_nomenclature
        self.label_gen = LabelGenerator(self.ui)

    def run(self):
        self.send_to_printer(self.weight, self.current_nomenclature)
        self.finished.emit()

    def send_to_printer(self, weight, current_nomenclature):
        self.label_gen.create_label(current_nomenclature, weight)


def get_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 4)
    return printers
