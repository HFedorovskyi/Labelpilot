from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot, QDate, QThread, Signal, QEvent
from scales_connections.ethernet_controller import EthernetController
from ui.ui_mainwindow import Ui_MainWindow
from scales_connections.serial_communications_controller import SerialController
from setting.settings_controller import SettingsController
from datebase.LabelCustom_datebase_controller import LabelCustomDbController
from views.numpad import NumPadController


class WorkerThread(QThread):
    finished = Signal()

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def run(self):
        self.controller.setup_connector()
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  #Создаём экземпляп класса MainWindows(), главное окно
        self.ui.setupUi(self)  # передаём экземплляр в setupUI
        self.ui.menuBtn.click()
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.stackedWidget.setCurrentIndex(
            0)  # Устнавливаем первый открывающийся виджет (На данный момент маркирвка без задания)
        self.settings_controller = SettingsController(self.ui, self)
        self.settings_controller.load_settings()
        self.datebase_controller = LabelCustomDbController(self.ui)
        self.change_controller()

        self.controller.setup_connector()
        self.controller.start()
        self.controller.set_weight_stable_timer()


        # Подключаем кнопки к методам
        self.ui.settingButn.clicked.connect(self.open_settings_menu)
        self.ui.settingButn_2.clicked.connect(self.open_settings_menu)
        self.ui.exitBnt.clicked.connect(self.close_app_menu)
        self.ui.exitBnt_2.clicked.connect(self.close_app_menu)
        self.ui.labelCustomBtn.clicked.connect(self.custom_labeling_menu)
        self.ui.labelCustomBtn_2.clicked.connect(self.custom_labeling_menu)
        self.ui.buttonGroup_2.idToggled.connect(self.change_controller)
        for item in (self.ui.ArticletextEdit, self.ui.weightPalletlineEdit, self.ui.batchNumberlineEdit):
            item.installEventFilter(self)


    @Slot()
    def open_settings_menu(self):  #Слот для открытия виджета настроек по клику
        self.controller.stop()
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def custom_labeling_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.centralwidget.setEnabled(False)
        self.settings_controller.load_settings()

        # Создаем поток и запускаем его
        self.thread1 = WorkerThread(self.controller)
        self.thread1.finished.connect(self.on_connector_setup_finished)
        self.thread1.start()

    @Slot()
    def on_connector_setup_finished(self):
        self.ui.centralwidget.setEnabled(True)
        self.controller.start()
        self.controller.set_weight_stable_timer()

    @Slot()
    def close_app_menu(self):  #Слот для выхода из приложения
        self.controller.stop()
        QApplication.quit()

    @Slot()
    def change_controller(self):
        if self.ui.buttonGroup_2.checkedId() == -3:
            self.controller = SerialController(self.ui)
        elif self.ui.buttonGroup_2.checkedId() == -4:
            self.controller = EthernetController(self.ui)

    def show_numpad(self, obj):
        self.numpad = NumPadController(self.ui, obj)
        self.numpad.setGeometry(obj.mapToGlobal(obj.rect().bottomLeft()).x() - 80,
                                obj.mapToGlobal(obj.rect().bottomLeft()).y(),
                                400, 400)
        self.numpad.show()

    def eventFilter(self, obj, event):
        obj_list = [self.ui.ArticletextEdit, self.ui.weightPalletlineEdit, self.ui.batchNumberlineEdit]
        if obj in obj_list and event.type() == QEvent.MouseButtonPress:
            self.show_numpad(obj)
            return True
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
