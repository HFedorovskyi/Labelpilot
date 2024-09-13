import threading
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ui.ui_mainwindow import Ui_MainWindow
from setting.settings_controller import SettingsController
from views.CustomLabel import CustomLabel
from app_logging.logging_config import logger
from http.server import HTTPServer
from client.connection_with_server import ConnectionsWithServer, StatusSender



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  #Создаём экземпляп класса MainWindows(), главное окно
        self.ui.setupUi(self)  # передаём экземплляр в setupUI
        self.ui.menuBtn.click()
        self.ui.menuBtn.click()
        self.status_sender = StatusSender()
        self.status_sender.send_status_to_server()
        self.ui.stackedWidget.setCurrentIndex(
            0)  # Устнавливаем первый открывающийся виджет (На данный момент маркирвка без задания)
        self.settings_controller = SettingsController(self.ui, self)
        self.settings_controller.load_settings()
        self.custom_label_page = CustomLabel(self.ui)
        self.start_server()
        # Подключаем кнопки к методам
        self.ui.settingButn.clicked.connect(self.open_settings_page)
        self.ui.settingButn_2.clicked.connect(self.open_settings_page)
        self.ui.exitBnt.clicked.connect(self.close_app_menu)
        self.ui.exitBnt_2.clicked.connect(self.close_app_menu)
        self.ui.labelCustomBtn.clicked.connect(self.open_custom_label_page)
        self.ui.labelCustomBtn_2.clicked.connect(self.open_custom_label_page)

    @Slot()
    def open_settings_page(self):
        self.custom_label_page.scale_connection.stop()
        self.custom_label_page.scale_connection.weight_stable_timer.stop()
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def open_custom_label_page(self):
        self.settings_controller.load_settings()
        self.custom_label_page.open_custom_label()

    @Slot()
    def close_app_menu(self):
        if not self.condition_close_window():
            self.show_error_window()
        else:
            self.custom_label_page.scale_connection.stop()
            QApplication.quit()

    def condition_close_window(self):
        box_on_pallet = self.custom_label_page.work_with_packs.boxes_worker.box_counter
        pack_on_box = self.custom_label_page.work_with_packs.pack_worker.pack_counter
        if box_on_pallet == 0 and pack_on_box == 0:
            return True
        return False

    def start_server(self):
        server_address = ('', 5005)
        print(type(self.custom_label_page.datebase_controller))
        ConnectionsWithServer.db_controller = self.custom_label_page.datebase_controller
        self.httpd = HTTPServer(server_address, ConnectionsWithServer)
        server_thread = threading.Thread(target=self.httpd.serve_forever)
        server_thread.daemon = True  # Поток завершится при закрытии приложения
        server_thread.start()

    def closeEvent(self, event):
        if not self.condition_close_window():
            event.ignore()
            self.show_error_window()
        else:

            self.custom_label_page.scale_connection.stop()
            self.httpd.shutdown()
            self.httpd.server_close()
            self.status_sender.timer.stop()
            QApplication.quit()

    def show_error_window(self):
        self.custom_label_page.work_with_packs.boxes_worker.show_error_window(3)

    def running_broadcast(self):
        broadcast_thread = threading.Thread(target=self.client.listen_broadcast)
        broadcast_thread.daemon = True
        broadcast_thread.start()
