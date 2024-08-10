from ui.dialog_window_close_box_error import Ui_BoxCloseError
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class CloseBoxError(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BoxCloseError()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Popup)

    def current_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)


