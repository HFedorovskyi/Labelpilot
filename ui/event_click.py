from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import Qt, QEvent


class ClickableWidget(QStackedWidget):

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

    def eventFilter(self, watched, event):
        if watched == self.stacked_widget and event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self.stacked_widget.setCurrentIndex(0)
                return True
        return super().eventFilter(watched, event)
