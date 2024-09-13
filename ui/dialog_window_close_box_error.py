# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'erroriNsiFc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)
import resource_rc
import resource_rc

class Ui_BoxCloseError(object):
    def setupUi(self, BoxCloseError):
        if not BoxCloseError.objectName():
            BoxCloseError.setObjectName(u"BoxCloseError")
        BoxCloseError.resize(400, 300)
        BoxCloseError.setMinimumSize(QSize(400, 300))
        BoxCloseError.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/icons/icons/printer_ztal8w3rcad8.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        BoxCloseError.setWindowIcon(icon)
        BoxCloseError.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"")
        self.stackedWidget = QStackedWidget(BoxCloseError)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 400, 300))
        self.stackedWidget.setMinimumSize(QSize(400, 300))
        self.stackedWidget.setMaximumSize(QSize(400, 300))
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(255, 204, 204);\n"
"}\n"
"")
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 200, 281, 71))
        self.pushButton.setMaximumSize(QSize(281, 71))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/confirm_tahgxsvfihik.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(50, 5016))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 366, 72))
        self.label.setMaximumSize(QSize(371, 111))
        self.label.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 10, 91, 91))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/packing_1imgzsd88lx9.svg"))
        self.label_3.setScaledContents(True)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, -10, 101, 91))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/empty_box_8h1s15gsh4mn.svg"))
        self.label_5.setScaledContents(True)
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 190, 281, 71))
        self.pushButton_3.setMaximumSize(QSize(281, 71))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(50, 5016))
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 81, 366, 101))
        self.label_6.setMaximumSize(QSize(371, 111))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.pushButton_4 = QPushButton(self.page_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 199, 281, 71))
        self.pushButton_4.setMaximumSize(QSize(281, 71))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(50, 5016))
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, -1, 101, 91))
        self.label_7.setPixmap(QPixmap(u":/icons/icons/pallet_4dj5cqpnmf6j.svg"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 366, 101))
        self.label_8.setMaximumSize(QSize(371, 111))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.pushButton_5 = QPushButton(self.page_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(60, 210, 281, 71))
        self.pushButton_5.setMaximumSize(QSize(281, 71))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(50, 5016))
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(190, 0, 91, 71))
        self.label_9.setPixmap(QPixmap(u":/icons/icons/pallet_4dj5cqpnmf6j.svg"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 80, 366, 120))
        self.label_10.setMaximumSize(QSize(371, 120))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, -10, 81, 81))
        self.label_11.setPixmap(QPixmap(u":/icons/icons/packing_1imgzsd88lx9.svg"))
        self.label_11.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_23 = QLabel(self.page_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 120, 366, 81))
        self.label_23.setMaximumSize(QSize(371, 120))
        self.label_23.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_24 = QLabel(self.page_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(130, 0, 121, 121))
        self.label_24.setPixmap(QPixmap(u":/icons/icons/forbidden_q9gv0dg6fncc.svg"))
        self.label_24.setScaledContents(True)
        self.pushButton_11 = QPushButton(self.page_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(60, 210, 281, 71))
        self.pushButton_11.setMaximumSize(QSize(281, 71))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(50, 5016))
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 0, 91, 91))
        self.label_4.setPixmap(QPixmap(u":/icons/icons/sku_mxdw1wuhf35o.svg"))
        self.label_4.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 190, 281, 71))
        self.pushButton_2.setMaximumSize(QSize(281, 71))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 9pt \"Comic Sans MS\";\n"
"	\n"
"	background-color: rgb(254, 135, 93);\n"
"}")
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(50, 5016))
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 366, 72))
        self.label_2.setMaximumSize(QSize(371, 111))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"	background-color: rgb(237, 243, 255);\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(BoxCloseError)
        self.pushButton_2.clicked["bool"].connect(BoxCloseError.close)
        self.pushButton.clicked["bool"].connect(BoxCloseError.close)
        self.pushButton_5.clicked["bool"].connect(BoxCloseError.close)
        self.pushButton_3.clicked["bool"].connect(BoxCloseError.close)
        self.pushButton_4.clicked["bool"].connect(BoxCloseError.close)
        self.pushButton_11.clicked["bool"].connect(BoxCloseError.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BoxCloseError)
    # setupUi

    def retranslateUi(self, BoxCloseError):
        BoxCloseError.setWindowTitle(QCoreApplication.translate("BoxCloseError", u"LabelPilot", None))
        self.pushButton.setText(QCoreApplication.translate("BoxCloseError", u"OK", None))
        self.label.setText(QCoreApplication.translate("BoxCloseError", u"\u041f\u0435\u0440\u0435\u0434 \u0437\u0430\u043a\u0440\u044b\u0442\u0438\u0435\u043c \u043f\u0430\u043b\u043b\u0435\u0442\u044b \u0437\u0430\u043a\u0440\u043e\u0439\u0442\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043e\u0440\u043e\u0431!", None))
        self.label_3.setText("")
        self.label_5.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("BoxCloseError", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("BoxCloseError", u"\u041d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u043e\u0439 \u043a\u043e\u0440\u043e\u0431! \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u0437\u0432\u0435\u0441\u0438\u0442\u044c \u0445\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u043d\u0443 \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0443!", None))
        self.pushButton_4.setText(QCoreApplication.translate("BoxCloseError", u"OK", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("BoxCloseError", u"\u041d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u043e\u0439 \u043f\u0430\u043b\u043b\u0435\u0442! \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0443\u043f\u0430\u043a\u043e\u0432\u0430\u0442\u044c \u0445\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u0438\u043d \u043a\u043e\u0440\u043e\u0431!", None))
        self.pushButton_5.setText(QCoreApplication.translate("BoxCloseError", u"OK", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("BoxCloseError", u"\u041e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0435 \u043a\u043e\u0440\u043e\u0431\u0430 \u0438\u043b\u0438 \u043f\u0430\u043b\u043b\u0435\u0442\u044b! \u0414\u043b\u044f \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0437\u0430\u043a\u0440\u044b\u0442\u044c \u0432\u0441\u0435 \u043a\u043e\u0440\u043e\u0431\u0430 \u0438 \u043f\u0430\u043b\u043b\u0435\u0442\u044b!", None))
        self.label_11.setText("")
        self.label_23.setText(QCoreApplication.translate("BoxCloseError", u"\u041d\u0435\u0442 \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a \u0434\u043b\u044f \u043e\u0442\u043c\u0435\u043d\u044b! \u041a\u043e\u0440\u043e\u0431 \u043f\u0443\u0441\u0442!", None))
        self.label_24.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("BoxCloseError", u"OK", None))
        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("BoxCloseError", u"\u041e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("BoxCloseError", u"\u0414\u043b\u044f \u0441\u043c\u0435\u043d\u0438 \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043a\u0440\u043e\u0439\u0442\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043e\u0440\u043e\u0431!", None))
    # retranslateUi

