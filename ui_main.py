# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color:#14213D;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: #14213D;")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setEnabled(False)
        self.frame_top.setStyleSheet(u"background-color:rgba(255,255,255,0)")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgba(35, 35, 35,0);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.frame_top_menus)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"EB Garamond Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnHome.setFont(font)
        self.btnHome.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHome.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnHome)

        self.btnCars = QPushButton(self.frame_top_menus)
        self.btnCars.setObjectName(u"btnCars")
        self.btnCars.setMinimumSize(QSize(0, 40))
        self.btnCars.setFont(font)
        self.btnCars.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCars.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnCars)

        self.btnNew = QPushButton(self.frame_top_menus)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setMinimumSize(QSize(0, 40))
        self.btnNew.setFont(font)
        self.btnNew.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNew.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnNew)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.label_10 = QLabel(self.homepage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 20, 481, 31))
        font1 = QFont()
        font1.setFamily(u"EB Garamond Medium")
        font1.setPointSize(18)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: #e5e5e5;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.homepage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 110, 631, 241))
        self.lineEdit_5 = QLineEdit(self.homepage)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(200, 390, 331, 21))
        font2 = QFont()
        font2.setFamily(u"EB Garamond Medium")
        font2.setPointSize(11)
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setStyleSheet(u"color: #e5e5e5;")
        self.btnNew_2 = QPushButton(self.homepage)
        self.btnNew_2.setObjectName(u"btnNew_2")
        self.btnNew_2.setGeometry(QRect(550, 380, 0, 40))
        self.btnNew_2.setMinimumSize(QSize(0, 40))
        self.btnNew_2.setFont(font)
        self.btnNew_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNew_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btnDelete_2 = QPushButton(self.homepage)
        self.btnDelete_2.setObjectName(u"btnDelete_2")
        self.btnDelete_2.setGeometry(QRect(550, 390, 111, 21))
        font3 = QFont()
        font3.setFamily(u"EB Garamond Medium")
        font3.setPointSize(12)
        self.btnDelete_2.setFont(font3)
        self.btnDelete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDelete_2.setStyleSheet(u"QPushButton {\n"
"	color:#e5e5e5;\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.homepage)
        self.cars = QWidget()
        self.cars.setObjectName(u"cars")
        self.tableWidget = QTableWidget(self.cars)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 120, 891, 281))
        self.btnView = QPushButton(self.cars)
        self.btnView.setObjectName(u"btnView")
        self.btnView.setGeometry(QRect(290, 430, 111, 31))
        font4 = QFont()
        font4.setFamily(u"EB Garamond Medium")
        font4.setPointSize(14)
        self.btnView.setFont(font4)
        self.btnView.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnView.setStyleSheet(u"background-color:#fca311;\n"
"border-radius: 8px;\n"
"color: #14213D;\n"
"border:none;\n"
"outline:none;\n"
"")
        self.btnDelete = QPushButton(self.cars)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(500, 430, 111, 31))
        self.btnDelete.setFont(font4)
        self.btnDelete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDelete.setStyleSheet(u"background-color:red;\n"
"border-radius: 8px;\n"
"color: #fff;\n"
"outline:none;\n"
"")
        self.label_9 = QLabel(self.cars)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 50, 481, 31))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: #e5e5e5;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.cars)
        self.new_car = QWidget()
        self.new_car.setObjectName(u"new_car")
        self.label = QLabel(self.new_car)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 50, 201, 41))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:#fff")
        self.label.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.new_car)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 120, 351, 151))
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"color:#fff")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 81, 16))
        self.label_2.setFont(font2)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 40, 181, 20))
        self.lineEdit.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 70, 181, 20))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(140, 100, 181, 20))
        self.lineEdit_3.setFont(font2)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 70, 91, 16))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 100, 47, 13))
        self.label_4.setFont(font2)
        self.groupBox_2 = QGroupBox(self.new_car)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(480, 120, 351, 151))
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setStyleSheet(u"color:#fff")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 40, 71, 16))
        self.label_5.setFont(font2)
        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(140, 40, 181, 20))
        self.lineEdit_4.setFont(font2)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 70, 61, 16))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 100, 71, 16))
        self.label_7.setFont(font2)
        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(140, 100, 181, 20))
        self.lineEdit_6.setFont(font2)
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(140, 70, 181, 22))
        self.positions = ['Lecturer', 'Staff']
        self.comboBox_2.addItems(self.positions)
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setFrame(True)
        self.label_8 = QLabel(self.new_car)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 310, 111, 16))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color:#fff;")
        self.comboBox = QComboBox(self.new_car)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 310, 201, 22))
        self.comboBox.setFont(font2)
        self.posts = ["Lecturers' Bay", "Staff Bay"]
        self.comboBox.addItems(self.posts)
        self.comboBox.setStyleSheet(u"color: #fff;")
        self.btnSave = QPushButton(self.new_car)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(380, 380, 111, 31))
        self.btnSave.setFont(font4)
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSave.setStyleSheet(u"background-color:#fca311;\n"
"border-radius: 8px;\n"
"color: #14213D;\n"
"border:none;\n"
"outline:none;\n"
"")
        self.stackedWidget.addWidget(self.new_car)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnCars.setText(QCoreApplication.translate("MainWindow", u"Vehicles", None))
        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"License PLate Recognition Homepage", None))
        self.label_11.setText("")
        self.btnNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btnDelete_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btnView.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"List of All Cars", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add a New Vehicle", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vehicle Details", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"License Plate", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ABC1234", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Toyota", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hilux GD6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vehicle Make", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Owner Details", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"National ID Nu", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12-12344567A89", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parking Area", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

