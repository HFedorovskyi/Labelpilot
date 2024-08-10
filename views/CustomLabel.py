from PySide6.QtCore import Slot, QDate, QThread, Signal, QEvent, QObject, QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup
import threading
from scales_connections.serial_controller import SerialController
from scales_connections.ethernet_controller import EthernetController
from ui.event_click import ClickableWidget
from views.numpad import NumPadController
from datebase.LabelCustom_datebase_controller import LabelCustomDbController, WorkingWithPacksController


class WorkerThread(QObject):
    finished = Signal()

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def run(self):
        self.controller.setup_connector()
        self.finished.emit()


class CustomLabel(QObject):
    METHOD_SCALE_CONNECTION = {
        -3: SerialController,
        -4: EthernetController
    }

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.datebase_controller = LabelCustomDbController(self.ui)
        self.work_with_packs = WorkingWithPacksController(self.ui)
        self.work_with_packs.fill_ContainerstreeWidget()
        self.chose_method_scale_connections()
        self.start_scale_connections()

        self.event_click_widget_3 = ClickableWidget(self.ui.stackedWidget_3)
        self.event_click_widget_4 = ClickableWidget(self.ui.stackedWidget_4)
        self.ui.stackedWidget_3.installEventFilter(self.event_click_widget_3)
        self.ui.stackedWidget_4.installEventFilter(self.event_click_widget_4)
        for item in (self.ui.ArticletextEdit, self.ui.weightPalletlineEdit, self.ui.batchNumberlineEdit):
            item.installEventFilter(self)

        self.ui.choseScaleConnectButtnGroup.idToggled.connect(self.chose_method_scale_connections)
        self.ui.labelCustomBtn.clicked.connect(self.open_custom_label)
        self.ui.labelCustomBtn_2.clicked.connect(self.open_custom_label)
        self.scale_connection.finish_weight_stability.connect(self.aaa)
        # self.ui.printPortionBtn.clicked.connect(lambda: self.animate_click(self.ui.printPortionBtn))

    @Slot()
    def chose_method_scale_connections(self):
        checked_id = self.ui.choseScaleConnectButtnGroup.checkedId()
        controller_class = self.METHOD_SCALE_CONNECTION.get(checked_id)
        self.scale_connection = controller_class(self.ui)

    def start_scale_connections(self):
        self.scale_connection.setup_connector()
        self.scale_connection.start()
        self.scale_connection.set_weight_stable_timer()

    @Slot()
    def open_custom_label(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.centralwidget.setEnabled(False)

        # Создаем поток и запускаем его
        self.thread1 = WorkerThread(self.scale_connection)
        self.thread1.finished.connect(self.on_connector_setup_finished)
        self.thread = threading.Thread(target=self.thread1.run)

        self.thread.start()

    @Slot()
    def on_connector_setup_finished(self):
        self.ui.centralwidget.setEnabled(True)
        self.scale_connection.start()
        self.scale_connection.set_weight_stable_timer()

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

    @Slot()
    def aaa(self):
        self.work_with_packs.write_to_ContainerstreeWidget(
            self.ui.indicationWeightNettotextBrowser.toPlainText(),
            self.ui.indicationWeightBruttoBrowser.toPlainText())

    # @staticmethod
    # def animate_click(button):
    #     # Получаем начальную геометрию кнопки
    #     start_geometry = button.geometry()
    #
    #     # Рассчитываем центр кнопки
    #     center = start_geometry.center()
    #
    #     # Рассчитываем уменьшенную геометрию кнопки
    #     shrink_geometry = start_geometry.adjusted(10, 10, 20, 20)
    #
    #     # Центрируем уменьшенную геометрию вокруг того же центра
    #     shrink_geometry.moveCenter(center)
    #
    #     # Создаем анимацию уменьшения
    #     shrink_animation = QPropertyAnimation(button, b"geometry")
    #     shrink_animation.setDuration(150)  # Длительность анимации уменьшения в миллисекундах
    #     shrink_animation.setEasingCurve(QEasingCurve.OutQuad)  # Кривая анимации уменьшения
    #     shrink_animation.setStartValue(start_geometry)
    #     shrink_animation.setEndValue(shrink_geometry)
    #
    #     # Создаем анимацию увеличения
    #     expand_animation = QPropertyAnimation(button, b"geometry")
    #     expand_animation.setDuration(150)  # Длительность анимации увеличения в миллисекундах
    #     expand_animation.setEasingCurve(QEasingCurve.OutQuad)  # Кривая анимации увеличения
    #     expand_animation.setStartValue(shrink_geometry)
    #     expand_animation.setEndValue(start_geometry)
    #
    #     # Создаем группу последовательных анимаций
    #     animation_group = QSequentialAnimationGroup()
    #     animation_group.addAnimation(shrink_animation)
    #     animation_group.addAnimation(expand_animation)
    #
    #     # Запускаем анимацию
    #     animation_group.start()

        # Сохраняем ссылку на анимацию, чтобы она не была уничтожена сборщиком мусора
        #button.animation_group = animation_group