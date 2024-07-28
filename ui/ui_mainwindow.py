# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledCoFgAB.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTextBrowser, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2016, 994)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1366, 768))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/printer_ztal8w3rcad8.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(1930, 1090))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(250, 768))
        self.widget_2.setMaximumSize(QSize(81, 1080))
        self.widget_2.setBaseSize(QSize(0, 0))
        self.widget_2.setToolTipDuration(-1)
        self.widget_2.setStyleSheet(u"background-color: rgb(31, 48, 74);")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 40, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/printer_ztal8w3rcad8_64.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 28pt \"Gabriola\";\n"
"color: white;")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(17, 127, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelTaskBtn = QPushButton(self.widget_2)
        self.labelTaskBtn.setObjectName(u"labelTaskBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelTaskBtn.sizePolicy().hasHeightForWidth())
        self.labelTaskBtn.setSizePolicy(sizePolicy2)
        self.labelTaskBtn.setMinimumSize(QSize(250, 60))
        self.labelTaskBtn.setMaximumSize(QSize(71, 60))
        self.labelTaskBtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/homework_xxbtdusz7gez.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.labelTaskBtn.setIcon(icon1)
        self.labelTaskBtn.setIconSize(QSize(60, 60))
        self.labelTaskBtn.setCheckable(True)
        self.labelTaskBtn.setChecked(False)
        self.labelTaskBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.labelTaskBtn)

        self.labelCustomBtn = QPushButton(self.widget_2)
        self.labelCustomBtn.setObjectName(u"labelCustomBtn")
        self.labelCustomBtn.setMinimumSize(QSize(250, 60))
        self.labelCustomBtn.setMaximumSize(QSize(250, 60))
        self.labelCustomBtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/price_1yqd9vgrxrbf.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.labelCustomBtn.setIcon(icon2)
        self.labelCustomBtn.setIconSize(QSize(60, 60))
        self.labelCustomBtn.setCheckable(True)
        self.labelCustomBtn.setChecked(False)
        self.labelCustomBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.labelCustomBtn)

        self.nomenclatureBtn = QPushButton(self.widget_2)
        self.nomenclatureBtn.setObjectName(u"nomenclatureBtn")
        self.nomenclatureBtn.setMinimumSize(QSize(250, 60))
        self.nomenclatureBtn.setMaximumSize(QSize(250, 60))
        self.nomenclatureBtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/list_pxqdz7ye1u4x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nomenclatureBtn.setIcon(icon3)
        self.nomenclatureBtn.setIconSize(QSize(60, 60))
        self.nomenclatureBtn.setCheckable(True)
        self.nomenclatureBtn.setChecked(False)
        self.nomenclatureBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.nomenclatureBtn)

        self.statisticsbtn = QPushButton(self.widget_2)
        self.statisticsbtn.setObjectName(u"statisticsbtn")
        self.statisticsbtn.setMinimumSize(QSize(250, 60))
        self.statisticsbtn.setMaximumSize(QSize(250, 60))
        self.statisticsbtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/report_0ok1e3gxilw0.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.statisticsbtn.setIcon(icon4)
        self.statisticsbtn.setIconSize(QSize(60, 60))
        self.statisticsbtn.setCheckable(True)
        self.statisticsbtn.setChecked(False)
        self.statisticsbtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.statisticsbtn)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(17, 207, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingButn = QPushButton(self.widget_2)
        self.settingButn.setObjectName(u"settingButn")
        self.settingButn.setMinimumSize(QSize(250, 60))
        self.settingButn.setMaximumSize(QSize(250, 16777215))
        self.settingButn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings_cjy7y94ude82.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingButn.setIcon(icon5)
        self.settingButn.setIconSize(QSize(60, 60))
        self.settingButn.setCheckable(True)
        self.settingButn.setChecked(False)
        self.settingButn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settingButn)

        self.user_button = QPushButton(self.widget_2)
        self.user_button.setObjectName(u"user_button")
        self.user_button.setMinimumSize(QSize(250, 60))
        self.user_button.setMaximumSize(QSize(250, 60))
        self.user_button.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/user_rx4lk96w730g.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_button.setIcon(icon6)
        self.user_button.setIconSize(QSize(60, 60))
        self.user_button.setCheckable(True)
        self.user_button.setChecked(False)
        self.user_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.user_button)

        self.infoBtn = QPushButton(self.widget_2)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(250, 60))
        self.infoBtn.setMaximumSize(QSize(250, 60))
        self.infoBtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/info_8eyvq4xyzfds.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon7)
        self.infoBtn.setIconSize(QSize(60, 60))
        self.infoBtn.setCheckable(True)
        self.infoBtn.setChecked(False)
        self.infoBtn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.exitBnt = QPushButton(self.widget_2)
        self.exitBnt.setObjectName(u"exitBnt")
        self.exitBnt.setMinimumSize(QSize(250, 60))
        self.exitBnt.setMaximumSize(QSize(250, 16777215))
        self.exitBnt.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: white;\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/emergency_exit_nop0pice1req.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exitBnt.setIcon(icon8)
        self.exitBnt.setIconSize(QSize(60, 60))
        self.exitBnt.setCheckable(True)
        self.exitBnt.setChecked(False)
        self.exitBnt.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exitBnt)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(0, 75))
        self.widget_3.setMaximumSize(QSize(16777215, 61))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuBtn = QPushButton(self.widget_3)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMaximumSize(QSize(70, 50))
        self.menuBtn.setTabletTracking(False)
        self.menuBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menuBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"    background-color :transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/menu_2d9l8s604nq4.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon9)
        self.menuBtn.setIconSize(QSize(50, 50))
        self.menuBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.menuBtn)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(61, 0))
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_14.addWidget(self.widget_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 61))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16666661))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(237, 243, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Comic Sans MS\";")

        self.verticalLayout_7.addWidget(self.label_5)

        self.ArticletextEdit = QLineEdit(self.page)
        self.ArticletextEdit.setObjectName(u"ArticletextEdit")
        self.ArticletextEdit.setMaximumSize(QSize(177, 16777215))
        self.ArticletextEdit.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.ArticletextEdit.setMaxLength(14)
        self.ArticletextEdit.setDragEnabled(False)
        self.ArticletextEdit.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.ArticletextEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 9pt \"Comic Sans MS\";")

        self.verticalLayout_8.addWidget(self.label_7)

        self.NomenclatureComboBox = QComboBox(self.page)
        self.NomenclatureComboBox.setObjectName(u"NomenclatureComboBox")
        self.NomenclatureComboBox.setStyleSheet(u"QComboBox {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440"
                        "\u0435\u043b\u043a\u043e\u0439 */\n"
"    background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"	background: white;\n"
"	selection-background-color: rgb(237, 243, 255);\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 50px; /* \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u044b\u0441\u043e\u0442\u044b \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    padding: 5px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: rgb(237, 243, 255);\n"
"    width: 15px;\n"
"    margin: 0px 0px 0px 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u044b\u0441\u043e"
                        "\u0442\u044b \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    height: 40px; /* \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0432\u044b\u0441\u043e\u0442\u044b \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
" }\n"
"")

        self.verticalLayout_8.addWidget(self.NomenclatureComboBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(170, 0))
        self.label_10.setMaximumSize(QSize(170, 16777215))
        self.label_10.setStyleSheet(u"font: 9pt \"Comic Sans MS\";")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.dateEdit = QDateEdit(self.page)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy3)
        self.dateEdit.setMinimumSize(QSize(170, 0))
        self.dateEdit.setMaximumSize(QSize(150, 16777215))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"\n"
"QDateEdit::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"\n"
"}\n"
"        QDateEdit::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            width: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440"
                        "\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }\n"
"\n"
"\n"
"\n"
"            QCalendarWidget QToolButton {\n"
"                height: 50px;\n"
"                width: 150px;\n"
"                color: white;\n"
"                font-size: 20px;\n"
"                icon-size: 60px, 60px;\n"
"                background-color: #2a82da;\n"
"                margin: 10px;\n"
"            }\n"
"            QCalendarWidget QMenu {\n"
"                width: 150px;\n"
"                color: white;\n"
"                font-size: 20px;\n"
"                background-color: #2a82da;\n"
"            }\n"
"            QCalendarWidget QSpinBox {\n"
"                width: 150px;\n"
"                font-size: 20px;\n"
"                color: white;\n"
"                background-color: #2a82da;\n"
"                selection-back"
                        "ground-color: #0a214c;\n"
"                selection-color: white;\n"
"            }\n"
"            QCalendarWidget QSpinBox::up-button {\n"
"                subcontrol-origin: border;\n"
"                subcontrol-position: top right;\n"
"                width: 50px;\n"
"            }\n"
"            QCalendarWidget QSpinBox::down-button {\n"
"                subcontrol-origin: border;\n"
"                subcontrol-position: bottom right;\n"
"                width: 50px;\n"
"            }\n"
"            \n"
"            QCalendarWidget QAbstractItemView:enabled {\n"
"                font-size: 40px;\n"
"                color: black;\n"
"                background-color: #ffffff;\n"
"                selection-background-color: #2a82da;\n"
"                selection-color: white;\n"
"            }\n"
"\n"
"")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 12pt \"Comic Sans MS\";")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.weightPalletlineEdit = QLineEdit(self.page)
        self.weightPalletlineEdit.setObjectName(u"weightPalletlineEdit")
        self.weightPalletlineEdit.setMaximumSize(QSize(150, 16777215))
        self.weightPalletlineEdit.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.weightPalletlineEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.weightPalletlineEdit.setMaxLength(8)
        self.weightPalletlineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.weightPalletlineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 12pt \"Comic Sans MS\";")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.batchNumberlineEdit = QLineEdit(self.page)
        self.batchNumberlineEdit.setObjectName(u"batchNumberlineEdit")
        self.batchNumberlineEdit.setMaximumSize(QSize(200, 16777215))
        self.batchNumberlineEdit.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.batchNumberlineEdit.setMaxLength(20)
        self.batchNumberlineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.batchNumberlineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 151))
        self.widget_5.setMaximumSize(QSize(16777215, 151))
        self.widget_5.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 9pt \"Comic Sans MS\";\n"
" border: white; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label_6)

        self.indicationWeightNettotextBrowser = QTextBrowser(self.widget_5)
        self.indicationWeightNettotextBrowser.setObjectName(u"indicationWeightNettotextBrowser")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.indicationWeightNettotextBrowser.setFont(font)
        self.indicationWeightNettotextBrowser.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 32pt \"Comic Sans MS\";\n"
"	text-align: center;\n"
"}\n"
"")
        self.indicationWeightNettotextBrowser.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.indicationWeightNettotextBrowser.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)

        self.verticalLayout_9.addWidget(self.indicationWeightNettotextBrowser)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 9pt \"Comic Sans MS\";\n"
" border: white; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"\n"
"")
        self.label_8.setTextFormat(Qt.TextFormat.AutoText)
        self.label_8.setScaledContents(False)

        self.verticalLayout_10.addWidget(self.label_8)

        self.indicationWeightBruttoBrowser = QTextBrowser(self.widget_5)
        self.indicationWeightBruttoBrowser.setObjectName(u"indicationWeightBruttoBrowser")
        self.indicationWeightBruttoBrowser.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 32pt \"Comic Sans MS\";\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.indicationWeightBruttoBrowser)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 9pt \"Comic Sans MS\";\n"
" border: white; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"\n"
"")

        self.verticalLayout_11.addWidget(self.label_9)

        self.conteinerWeightTextBrowser = QTextBrowser(self.widget_5)
        self.conteinerWeightTextBrowser.setObjectName(u"conteinerWeightTextBrowser")
        self.conteinerWeightTextBrowser.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 32pt \"Comic Sans MS\";\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.conteinerWeightTextBrowser)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_5)


        self.verticalLayout_13.addWidget(self.widget_5)

        self.ContainerstreeWidget = QTreeWidget(self.page)
        self.ContainerstreeWidget.setObjectName(u"ContainerstreeWidget")
        self.ContainerstreeWidget.setStyleSheet(u"QTreeWidget{\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 12pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.ContainerstreeWidget.setAlternatingRowColors(True)
        self.ContainerstreeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ContainerstreeWidget.setUniformRowHeights(False)
        self.ContainerstreeWidget.setAnimated(True)
        self.ContainerstreeWidget.header().setCascadingSectionResizes(True)
        self.ContainerstreeWidget.header().setMinimumSectionSize(50)
        self.ContainerstreeWidget.header().setHighlightSections(False)

        self.verticalLayout_13.addWidget(self.ContainerstreeWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(251, 82))
        self.pushButton_4.setMaximumSize(QSize(251, 82))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/cancel_o8dj9cqxmwbl.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(60, 1660))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(251, 82))
        self.pushButton_5.setMaximumSize(QSize(251, 82))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/repeat_qlrg067k4jxk.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(60, 1660))

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(251, 82))
        self.pushButton_6.setMaximumSize(QSize(251, 82))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/survey_nsuh0eeoyu2z.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon12)
        self.pushButton_6.setIconSize(QSize(60, 1660))

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.printPortionBtn = QPushButton(self.page)
        self.printPortionBtn.setObjectName(u"printPortionBtn")
        self.printPortionBtn.setMinimumSize(QSize(251, 82))
        self.printPortionBtn.setMaximumSize(QSize(251, 82))
        self.printPortionBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/label_62lcqagmtpj0.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.printPortionBtn.setIcon(icon13)
        self.printPortionBtn.setIconSize(QSize(60, 1660))
        self.printPortionBtn.setCheckable(False)
        self.printPortionBtn.setFlat(False)

        self.gridLayout.addWidget(self.printPortionBtn, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(251, 82))
        self.pushButton_3.setMaximumSize(QSize(251, 82))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/stock_4kvw2mm2kfh3.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon14)
        self.pushButton_3.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(251, 82))
        self.pushButton_2.setMaximumSize(QSize(251, 82))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(84, 147, 230);\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/open_box_2qidrxnyisj5.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QSize(60, 1660))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_21 = QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tabWidget_2 = QTabWidget(self.page_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy4)
        self.tabWidget_2.setMinimumSize(QSize(0, 768))
        self.tabWidget_2.setStyleSheet(u"            QTabWidget::tab-bar {\n"
"                alignment: left;\n"
"            }\n"
"\n"
"            QTabBar::tab {\n"
"                background: #FFFFFF;\n"
"                \n"
"                border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"                border-top-left-radius: 4px;\n"
"                border-top-right-radius: 4px;\n"
"                min-width: 8ex;\n"
"                padding: 10px;\n"
"                margin-right: 2px;\n"
"            }\n"
"\n"
"            QTabBar::tab:selected, QTabBar::tab:hover {\n"
"                background: rgb(137, 159, 255);\n"
"                border-color: #9B9B9B;\n"
"            }\n"
"\n"
"            QTabBar::tab:selected {\n"
"                margin-bottom: -1px; /* prevent double border on tab selected */\n"
"            }\n"
"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_4 = QWidget(self.tab_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(9, 9, 1543, 71))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.checkBoxWeightStablity = QCheckBox(self.widget_4)
        self.checkBoxWeightStablity.setObjectName(u"checkBoxWeightStablity")
        self.checkBoxWeightStablity.setGeometry(QRect(10, 10, 331, 35))
        self.checkBoxWeightStablity.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/icons/icons/cancel_nnivzmi7quma.svg);\n"
"    background-color: #b0b0b0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border: 2px solid #b0b0b0; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/icons/icons/check_du9eye0oswbt.svg);\n"
"    background-color: #4caf50; /* \u0426"
                        "\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border: 2px solid #4caf50; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #e0e0e0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #66bb6a; /* \u0426\u0432\u0435\u0442"
                        " \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: #c0c0c0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: #388e3c; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"")
        self.widget_6 = QWidget(self.tab_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 100, 1543, 111))
        self.widget_6.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.checkBoxBatchUse = QCheckBox(self.widget_6)
        self.checkBoxBatchUse.setObjectName(u"checkBoxBatchUse")
        self.checkBoxBatchUse.setGeometry(QRect(10, 10, 331, 35))
        self.checkBoxBatchUse.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/icons/icons/cancel_nnivzmi7quma.svg);\n"
"    background-color: #b0b0b0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border: 2px solid #b0b0b0; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/icons/icons/check_du9eye0oswbt.svg);\n"
"    background-color: #4caf50; /* \u0426"
                        "\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border: 2px solid #4caf50; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #e0e0e0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #66bb6a; /* \u0426\u0432\u0435\u0442"
                        " \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: #c0c0c0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: #388e3c; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u0434\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"")
        self.saveSetting_2 = QPushButton(self.tab_3)
        self.saveSetting_2.setObjectName(u"saveSetting_2")
        self.saveSetting_2.setGeometry(QRect(20, 660, 250, 60))
        self.saveSetting_2.setMinimumSize(QSize(250, 60))
        self.saveSetting_2.setMaximumSize(QSize(250, 60))
        self.saveSetting_2.setStyleSheet(u"QPushButton {\n"
"\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"color: rgb(68, 64, 194);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.saveSetting_2.setIconSize(QSize(30, 30))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_16 = QVBoxLayout(self.tab_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_9 = QWidget(self.tab_4)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy5)
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.widget_9.setMaximumSize(QSize(1000, 50))
        self.widget_9.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.checkBox = QCheckBox(self.widget_9)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(383, 12, 73, 34))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    border: 2px solid #3f51b5; /* \u0421\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    background-color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #3f51b5;\n"
"    border-radius: 10px;\n"
"    \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.449438 rgba(25, 34, 87, 255), stop:0.539326 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px"
                        " solid #3f51b5;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"    padding: 5px;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);\n"
"}\n"
"")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.comConnectCheckBox = QCheckBox(self.widget_9)
        self.buttonGroup_2.addButton(self.comConnectCheckBox)
        self.comConnectCheckBox.setObjectName(u"comConnectCheckBox")
        self.comConnectCheckBox.setGeometry(QRect(287, 12, 77, 34))
        self.comConnectCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    border: 2px solid #3f51b5; /* \u0421\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    background-color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #3f51b5;\n"
"    border-radius: 10px;\n"
"    \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.449438 rgba(25, 34, 87, 255), stop:0.539326 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px"
                        " solid #3f51b5;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"    padding: 5px;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);\n"
"}\n"
"")
        self.comConnectCheckBox.setChecked(False)
        self.comConnectCheckBox.setTristate(False)
        self.label_34 = QLabel(self.widget_9)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(9, 11, 164, 37))
        self.label_34.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")
        self.ethernetConnectCheckBox_ = QCheckBox(self.widget_9)
        self.buttonGroup_2.addButton(self.ethernetConnectCheckBox_)
        self.ethernetConnectCheckBox_.setObjectName(u"ethernetConnectCheckBox_")
        self.ethernetConnectCheckBox_.setGeometry(QRect(179, 12, 102, 34))
        self.ethernetConnectCheckBox_.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    border: 2px solid #3f51b5; /* \u0421\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    background-color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #3f51b5;\n"
"    border-radius: 10px;\n"
"    \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.449438 rgba(25, 34, 87, 255), stop:0.539326 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px"
                        " solid #3f51b5;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"    padding: 5px;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);\n"
"}\n"
"")
        self.ethernetConnectCheckBox_.setChecked(True)
        self.ethernetConnectCheckBox_.setTristate(False)

        self.verticalLayout_16.addWidget(self.widget_9)

        self.stackedWidget_2 = QStackedWidget(self.tab_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QSize(0, 190))
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 190))
        self.stackedWidget_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.stackedWidget_2.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.stackedWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_6 = QGridLayout(self.page_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_36 = QLabel(self.page_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(41, 41))
        self.label_36.setMaximumSize(QSize(41, 41))
        self.label_36.setPixmap(QPixmap(u":/icons/icons/ip_address_m6qvx2qa4gd0 (1).svg"))
        self.label_36.setScaledContents(True)
        self.label_36.setWordWrap(False)

        self.gridLayout_3.addWidget(self.label_36, 0, 0, 1, 1)

        self.flabel_13 = QLabel(self.page_7)
        self.flabel_13.setObjectName(u"flabel_13")
        self.flabel_13.setMaximumSize(QSize(145, 48))
        self.flabel_13.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.gridLayout_3.addWidget(self.flabel_13, 0, 1, 1, 1)

        self.setIPlineEdit = QLineEdit(self.page_7)
        self.setIPlineEdit.setObjectName(u"setIPlineEdit")
        self.setIPlineEdit.setMinimumSize(QSize(201, 51))
        self.setIPlineEdit.setMaximumSize(QSize(201, 16777215))
        self.setIPlineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.setIPlineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.setIPlineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setIPlineEdit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.setIPlineEdit, 1, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_37 = QLabel(self.page_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(41, 41))
        self.label_37.setMaximumSize(QSize(41, 41))
        self.label_37.setPixmap(QPixmap(u":/icons/icons/connector_i86sbig2dy95.svg"))
        self.label_37.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_38 = QLabel(self.page_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(142, 41))
        self.label_38.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")
        self.label_38.setScaledContents(False)

        self.gridLayout_4.addWidget(self.label_38, 0, 1, 1, 1)

        self.setNetworkPortlineEdit = QLineEdit(self.page_7)
        self.setNetworkPortlineEdit.setObjectName(u"setNetworkPortlineEdit")
        self.setNetworkPortlineEdit.setMinimumSize(QSize(191, 51))
        self.setNetworkPortlineEdit.setMaximumSize(QSize(191, 16777215))
        self.setNetworkPortlineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.setNetworkPortlineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.setNetworkPortlineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setNetworkPortlineEdit.setDragEnabled(False)
        self.setNetworkPortlineEdit.setReadOnly(False)
        self.setNetworkPortlineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.setNetworkPortlineEdit.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.setNetworkPortlineEdit, 1, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_39 = QLabel(self.page_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(41, 41))
        self.label_39.setMaximumSize(QSize(41, 41))
        self.label_39.setPixmap(QPixmap(u":/icons/icons/scale_mjyoc8pn5u8b.svg"))
        self.label_39.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_40 = QLabel(self.page_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(350, 0))
        self.label_40.setMaximumSize(QSize(419, 16777215))
        self.label_40.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.gridLayout_5.addWidget(self.label_40, 0, 1, 1, 1)

        self.ListScalecomboBox = QComboBox(self.page_7)
        self.ListScalecomboBox.setObjectName(u"ListScalecomboBox")
        self.ListScalecomboBox.setEnabled(True)
        self.ListScalecomboBox.setMinimumSize(QSize(400, 51))
        self.ListScalecomboBox.setMaximumSize(QSize(477, 16777215))
        self.ListScalecomboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }")

        self.gridLayout_5.addWidget(self.ListScalecomboBox, 1, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 3, 1, 1)

        self.label_41 = QLabel(self.page_7)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QSize(0, 150))
        self.label_41.setMaximumSize(QSize(100, 16777215))
        self.label_41.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_41.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_41, 0, 4, 2, 1)

        self.horizontalSpacer = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.checkConnectionScaleNetworkBtn_2 = QPushButton(self.page_7)
        self.checkConnectionScaleNetworkBtn_2.setObjectName(u"checkConnectionScaleNetworkBtn_2")
        self.checkConnectionScaleNetworkBtn_2.setMinimumSize(QSize(150, 51))
        self.checkConnectionScaleNetworkBtn_2.setMaximumSize(QSize(150, 51))
        self.checkConnectionScaleNetworkBtn_2.setStyleSheet(u"QPushButton {\n"
"\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"color: rgb(68, 64, 194);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.checkConnectionScaleNetworkBtn_2.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.checkConnectionScaleNetworkBtn_2, 1, 0, 1, 1)

        self.label_35 = QLabel(self.page_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(650, 35))
        self.label_35.setMaximumSize(QSize(650, 35))
        self.label_35.setStyleSheet(u"font: 700 8pt \"Segoe UI\";")

        self.gridLayout_6.addWidget(self.label_35, 1, 1, 1, 3)

        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_10 = QGridLayout(self.page_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_42 = QLabel(self.page_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(48, 41))
        self.label_42.setMaximumSize(QSize(48, 41))
        self.label_42.setPixmap(QPixmap(u":/icons/icons/usb_trmvzo2325cj.svg"))
        self.label_42.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_43 = QLabel(self.page_8)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.gridLayout_9.addWidget(self.label_43, 0, 1, 1, 1)

        self.ChoseComPortcomboBox = QComboBox(self.page_8)
        self.ChoseComPortcomboBox.setObjectName(u"ChoseComPortcomboBox")
        self.ChoseComPortcomboBox.setMinimumSize(QSize(200, 51))
        self.ChoseComPortcomboBox.setMaximumSize(QSize(181, 16777215))
        self.ChoseComPortcomboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }")

        self.gridLayout_9.addWidget(self.ChoseComPortcomboBox, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_44 = QLabel(self.page_8)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(48, 41))
        self.label_44.setMaximumSize(QSize(48, 41))
        self.label_44.setPixmap(QPixmap(u":/icons/icons/scale_mjyoc8pn5u8b.svg"))
        self.label_44.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_44, 0, 0, 1, 1)

        self.label_45 = QLabel(self.page_8)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(521, 16777215))
        self.label_45.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.gridLayout_8.addWidget(self.label_45, 0, 1, 1, 1)

        self.ListScalecomboBox_2 = QComboBox(self.page_8)
        self.ListScalecomboBox_2.setObjectName(u"ListScalecomboBox_2")
        self.ListScalecomboBox_2.setMinimumSize(QSize(579, 51))
        self.ListScalecomboBox_2.setMaximumSize(QSize(579, 16777215))
        self.ListScalecomboBox_2.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }")

        self.gridLayout_8.addWidget(self.ListScalecomboBox_2, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 1, 1, 1)

        self.label_46 = QLabel(self.page_8)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(250, 100))
        self.label_46.setMaximumSize(QSize(250, 100))
        self.label_46.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.label_46.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_46, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(455, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 175, -1)
        self.checkConnectionScaleBtn = QPushButton(self.page_8)
        self.checkConnectionScaleBtn.setObjectName(u"checkConnectionScaleBtn")
        self.checkConnectionScaleBtn.setMinimumSize(QSize(201, 51))
        self.checkConnectionScaleBtn.setMaximumSize(QSize(201, 16777215))
        self.checkConnectionScaleBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"color: rgb(68, 64, 194);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.checkConnectionScaleBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.checkConnectionScaleBtn)

        self.label_47 = QLabel(self.page_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(700, 16777215))
        self.label_47.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_47)


        self.gridLayout_10.addLayout(self.horizontalLayout_7, 1, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(455, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.stackedWidget_2.addWidget(self.page_8)

        self.verticalLayout_16.addWidget(self.stackedWidget_2)

        self.progressBar = QProgressBar(self.tab_4)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy6)
        self.progressBar.setMinimumSize(QSize(1000, 0))
        self.progressBar.setMaximumSize(QSize(1800, 15))
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_16.addWidget(self.progressBar)

        self.verticalSpacer_6 = QSpacerItem(20, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)

        self.widget_10 = QWidget(self.tab_4)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy7)
        self.widget_10.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 14pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.gridLayout_7 = QGridLayout(self.widget_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_48 = QLabel(self.widget_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(300, 0))
        self.label_48.setMaximumSize(QSize(300, 16777215))
        self.label_48.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_48)

        self.chosePrinterPortionLabelComboBox = QComboBox(self.widget_10)
        self.chosePrinterPortionLabelComboBox.setObjectName(u"chosePrinterPortionLabelComboBox")
        self.chosePrinterPortionLabelComboBox.setMinimumSize(QSize(579, 51))
        self.chosePrinterPortionLabelComboBox.setMaximumSize(QSize(579, 16777215))
        self.chosePrinterPortionLabelComboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }\n"
"")
        self.chosePrinterPortionLabelComboBox.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.chosePrinterPortionLabelComboBox)


        self.gridLayout_7.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_49 = QLabel(self.widget_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(300, 0))
        self.label_49.setMaximumSize(QSize(300, 16777215))
        self.label_49.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_49)

        self.chosePrinterSumLabelComboBox = QComboBox(self.widget_10)
        self.chosePrinterSumLabelComboBox.setObjectName(u"chosePrinterSumLabelComboBox")
        self.chosePrinterSumLabelComboBox.setMinimumSize(QSize(579, 51))
        self.chosePrinterSumLabelComboBox.setMaximumSize(QSize(579, 16777215))
        self.chosePrinterSumLabelComboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.chosePrinterSumLabelComboBox)


        self.gridLayout_7.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_50 = QLabel(self.widget_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(300, 0))
        self.label_50.setMaximumSize(QSize(300, 16777215))
        self.label_50.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(68, 64, 194);")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_50)

        self.chosePrinterSPalLabelComboBox = QComboBox(self.widget_10)
        self.chosePrinterSPalLabelComboBox.setObjectName(u"chosePrinterSPalLabelComboBox")
        self.chosePrinterSPalLabelComboBox.setMinimumSize(QSize(550, 51))
        self.chosePrinterSPalLabelComboBox.setMaximumSize(QSize(579, 16777215))
        self.chosePrinterSPalLabelComboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font: 16pt \"Segoe UI\"; /* \u0428\u0440\u0438\u0444\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down_arrow_gmceuz4sicdl.svg);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            wid"
                        "th: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u0441\u043e \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0439 */\n"
"            background: transparent; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 */\n"
"        }")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.chosePrinterSPalLabelComboBox)


        self.gridLayout_7.addLayout(self.formLayout_3, 2, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_10)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.saveSetting = QPushButton(self.tab_4)
        self.saveSetting.setObjectName(u"saveSetting")
        self.saveSetting.setMinimumSize(QSize(250, 60))
        self.saveSetting.setMaximumSize(QSize(250, 60))
        self.saveSetting.setStyleSheet(u"QPushButton {\n"
"\n"
"    border-radius: 25px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"color: rgb(68, 64, 194);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.saveSetting.setIconSize(QSize(30, 30))

        self.verticalLayout_16.addWidget(self.saveSetting)

        self.verticalSpacer_7 = QSpacerItem(20, 231, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_21.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_14.addWidget(self.stackedWidget)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(81, 768))
        self.widget.setMaximumSize(QSize(81, 1080))
        self.widget.setStyleSheet(u"background-color: rgb(31, 48, 74);")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, -1, -1, -1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/printer_ztal8w3rcad8_64.png"))

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTaskBtn_2 = QPushButton(self.widget)
        self.labelTaskBtn_2.setObjectName(u"labelTaskBtn_2")
        sizePolicy2.setHeightForWidth(self.labelTaskBtn_2.sizePolicy().hasHeightForWidth())
        self.labelTaskBtn_2.setSizePolicy(sizePolicy2)
        self.labelTaskBtn_2.setMinimumSize(QSize(71, 60))
        self.labelTaskBtn_2.setMaximumSize(QSize(71, 60))
        self.labelTaskBtn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.labelTaskBtn_2.setIcon(icon1)
        self.labelTaskBtn_2.setIconSize(QSize(60, 60))
        self.labelTaskBtn_2.setCheckable(True)
        self.labelTaskBtn_2.setChecked(False)
        self.labelTaskBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.labelTaskBtn_2)

        self.labelCustomBtn_2 = QPushButton(self.widget)
        self.labelCustomBtn_2.setObjectName(u"labelCustomBtn_2")
        self.labelCustomBtn_2.setMinimumSize(QSize(71, 60))
        self.labelCustomBtn_2.setMaximumSize(QSize(71, 60))
        self.labelCustomBtn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.labelCustomBtn_2.setIcon(icon2)
        self.labelCustomBtn_2.setIconSize(QSize(60, 60))
        self.labelCustomBtn_2.setCheckable(True)
        self.labelCustomBtn_2.setChecked(False)
        self.labelCustomBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.labelCustomBtn_2)

        self.nomenclatureBtn_2 = QPushButton(self.widget)
        self.nomenclatureBtn_2.setObjectName(u"nomenclatureBtn_2")
        self.nomenclatureBtn_2.setMinimumSize(QSize(71, 60))
        self.nomenclatureBtn_2.setMaximumSize(QSize(71, 60))
        self.nomenclatureBtn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.nomenclatureBtn_2.setIcon(icon3)
        self.nomenclatureBtn_2.setIconSize(QSize(60, 60))
        self.nomenclatureBtn_2.setCheckable(True)
        self.nomenclatureBtn_2.setChecked(False)
        self.nomenclatureBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.nomenclatureBtn_2)

        self.statisticsBtn_2 = QPushButton(self.widget)
        self.statisticsBtn_2.setObjectName(u"statisticsBtn_2")
        self.statisticsBtn_2.setMinimumSize(QSize(71, 60))
        self.statisticsBtn_2.setMaximumSize(QSize(71, 60))
        self.statisticsBtn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.statisticsBtn_2.setIcon(icon4)
        self.statisticsBtn_2.setIconSize(QSize(60, 60))
        self.statisticsBtn_2.setCheckable(True)
        self.statisticsBtn_2.setChecked(False)
        self.statisticsBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.statisticsBtn_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.settingButn_2 = QPushButton(self.widget)
        self.settingButn_2.setObjectName(u"settingButn_2")
        self.settingButn_2.setMinimumSize(QSize(71, 60))
        self.settingButn_2.setMaximumSize(QSize(71, 16777215))
        self.settingButn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.settingButn_2.setIcon(icon5)
        self.settingButn_2.setIconSize(QSize(60, 60))
        self.settingButn_2.setCheckable(True)
        self.settingButn_2.setChecked(False)
        self.settingButn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settingButn_2)

        self.user_button_2 = QPushButton(self.widget)
        self.user_button_2.setObjectName(u"user_button_2")
        self.user_button_2.setMinimumSize(QSize(71, 60))
        self.user_button_2.setMaximumSize(QSize(71, 60))
        self.user_button_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.user_button_2.setIcon(icon6)
        self.user_button_2.setIconSize(QSize(60, 60))
        self.user_button_2.setCheckable(True)
        self.user_button_2.setChecked(False)
        self.user_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.user_button_2)

        self.infoBtn_2 = QPushButton(self.widget)
        self.infoBtn_2.setObjectName(u"infoBtn_2")
        self.infoBtn_2.setMinimumSize(QSize(71, 60))
        self.infoBtn_2.setMaximumSize(QSize(71, 60))
        self.infoBtn_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.infoBtn_2.setIcon(icon7)
        self.infoBtn_2.setIconSize(QSize(60, 60))
        self.infoBtn_2.setCheckable(True)
        self.infoBtn_2.setChecked(False)
        self.infoBtn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.infoBtn_2)

        self.exitBnt_2 = QPushButton(self.widget)
        self.exitBnt_2.setObjectName(u"exitBnt_2")
        self.exitBnt_2.setMinimumSize(QSize(71, 60))
        self.exitBnt_2.setMaximumSize(QSize(71, 60))
        self.exitBnt_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    background-color: rgb(102, 194, 255);\n"
"}")
        self.exitBnt_2.setIcon(icon8)
        self.exitBnt_2.setIconSize(QSize(60, 60))
        self.exitBnt_2.setCheckable(True)
        self.exitBnt_2.setChecked(False)
        self.exitBnt_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.exitBnt_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.nomenclatureBtn.toggled.connect(self.nomenclatureBtn_2.setChecked)
        self.menuBtn.toggled.connect(self.widget.setHidden)
        self.settingButn.toggled.connect(self.settingButn_2.setChecked)
        self.menuBtn.toggled.connect(self.widget_2.setVisible)
        self.labelCustomBtn.toggled.connect(self.labelCustomBtn_2.setChecked)
        self.infoBtn.toggled.connect(self.infoBtn_2.setChecked)
        self.user_button.toggled.connect(self.user_button_2.setChecked)
        self.exitBnt.toggled.connect(self.exitBnt_2.setChecked)
        self.labelTaskBtn.toggled.connect(self.labelTaskBtn_2.setChecked)
        self.statisticsbtn.toggled.connect(self.statisticsBtn_2.setChecked)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LabelPilot", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"LabelPilot", None))
        self.labelTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u0438\u044e", None))
        self.labelCustomBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u0431\u0435\u0437 \u0437\u0430\u0434\u0430\u043d\u0438\u044f   ", None))
        self.nomenclatureBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b", None))
        self.statisticsbtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442\u044b \u043e \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0435     ", None))
        self.settingButn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438                 ", None))
        self.user_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c             ", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435             ", None))
        self.exitBnt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434                        ", None))
        self.menuBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e, \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c!</span><br/><span style=\" font-size:9pt;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 LabelPilot.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0410\u0440\u0442\u0438\u043a\u0443\u043b</span></p></body></html>", None))
        self.ArticletextEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u043f\u0430\u043b\u043b\u0435\u0442\u044b, \u043a\u0433:", None))
        self.weightPalletlineEdit.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0440\u0442\u0438\u0438:", None))
        self.batchNumberlineEdit.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0412\u0435\u0441 \u043d\u0435\u0442\u0442\u043e</span></p></body></html>", None))
        self.indicationWeightNettotextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0412\u0435\u0441 \u0431\u0440\u0443\u0442\u0442\u043e</span></p></body></html>", None))
        self.indicationWeightBruttoBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0412\u0435\u0441 \u0442\u0430\u0440\u044b</span></p></body></html>", None))
        self.conteinerWeightTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        ___qtreewidgetitem = self.ContainerstreeWidget.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u043b\u043b\u0435\u0442\u044b", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u043e\u0440\u043e\u0431\u0430", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u0431\u0440\u0443\u0442\u0442\u043e", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u043d\u0435\u0442\u0442\u043e", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u044d\u0442\u0438\u043a\u0435\u0442\u043a\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u044d\u0442\u0438\u043a\u0435\u0442\u043a\u0438", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442\u043e\u0432\u043e\u0439 \u044d\u0442\u0438\u043a\u0435\u0442\u043a\u0438", None))
        self.printPortionBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u043e\u0439 \u044d\u0442\u0438\u043a\u0435\u0442\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043b\u043b\u0435\u0442\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043a\u043e\u0440\u043e\u0431\u043a\u0443", None))
        self.checkBoxWeightStablity.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u043f\u043e \u0441\u0442\u0430\u0431\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0432\u0435\u0441\u0430", None))
        self.checkBoxBatchUse.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u0442\u0438\u0438", None))
        self.saveSetting_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"WIFI", None))
        self.comConnectCheckBox.setText(QCoreApplication.translate("MainWindow", u"COM", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f:", None))
        self.ethernetConnectCheckBox_.setText(QCoreApplication.translate("MainWindow", u"Ethernet", None))
        self.label_36.setText("")
        self.flabel_13.setText(QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441", None))
        self.setIPlineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000.000;*", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u0435\u0432\u043e\u0439 \u043f\u043e\u0440\u0442", None))
        self.setNetworkPortlineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"00000;*", None))
        self.setNetworkPortlineEdit.setText(QCoreApplication.translate("MainWindow", u"12345", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0432\u0435\u0441\u0430\u043c", None))
        self.label_41.setText("")
        self.checkConnectionScaleNetworkBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.label_35.setText("")
        self.label_42.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"COM-\u043f\u043e\u0440\u0442", None))
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0432\u0435\u0441\u0430\u043c", None))
        self.label_46.setText("")
        self.checkConnectionScaleBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.label_47.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0435\u0442\u0440 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u043e\u0439 \u044d\u0442\u0438\u043a\u0442\u0435\u043a\u0438:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0435\u0442\u0440 \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0439 \u044d\u0442\u0438\u043a\u0442\u0435\u043a\u0438:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440 \u043f\u0430\u043b\u043b\u0435\u0442\u043d\u043e\u0433\u043e \u043b\u0438\u0441\u0442\u0430:", None))
        self.saveSetting.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044e", None))
        self.label_3.setText("")
        self.labelTaskBtn_2.setText("")
        self.labelCustomBtn_2.setText("")
        self.nomenclatureBtn_2.setText("")
        self.statisticsBtn_2.setText("")
        self.settingButn_2.setText("")
        self.user_button_2.setText("")
        self.infoBtn_2.setText("")
        self.exitBnt_2.setText("")
    # retranslateUi

