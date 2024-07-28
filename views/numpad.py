from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from ui.customs_ui import NumPadForm


class NumPadController(QWidget):

    def __init__(self, main_ui, obj):
        super().__init__()
        self.setWindowFlags(Qt.Popup)
        self.mainUI = main_ui
        self.ui = NumPadForm()
        self.ui.setupUi(self)
        self.initUI()
        self.obj = obj

    def initUI(self):
        self.ui.pushButton.clicked.connect(lambda: self.num_clicked('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.num_clicked('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.num_clicked('3'))
        self.ui.pushButton_5.clicked.connect(lambda: self.num_clicked('4'))
        self.ui.pushButton_6.clicked.connect(lambda: self.num_clicked('5'))
        self.ui.pushButton_4.clicked.connect(lambda: self.num_clicked('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.num_clicked('7'))
        self.ui.pushButton_9.clicked.connect(lambda: self.num_clicked('8'))
        self.ui.pushButton_8.clicked.connect(lambda: self.num_clicked('9'))
        self.ui.pushButton_10.clicked.connect(lambda: self.num_clicked('0'))
        self.ui.pushButton_11.clicked.connect(self.del_clicked)
        self.ui.pushButton_12.clicked.connect(lambda: self.num_clicked('.'))

    def num_clicked(self, num):
        current_text = self.obj.text()
        new_text = current_text + num
        self.obj.setText(new_text)

    def del_clicked(self):
        current_text = self.obj.text()
        new_text = current_text[:-1]
        self.obj.setText(new_text)



    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.close()


