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
		MainWindow.resize(1100, 600)
		MainWindow.setMinimumSize(QSize(1000, 500))
		MainWindow.setMaximumSize(QSize(1100, 650))
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
		font1 = QFont()
		font1.setPointSize(12)
		self.stackedWidget.setFont(font1)
		self.homepage = QWidget()
		self.homepage.setObjectName(u"homepage")
		self.label_10 = QLabel(self.homepage)
		self.label_10.setObjectName(u"label_10")
		self.label_10.setGeometry(QRect(230, 20, 481, 31))
		font2 = QFont()
		font2.setFamily(u"EB Garamond Medium")
		font2.setPointSize(18)
		self.label_10.setFont(font2)
		self.label_10.setStyleSheet(u"color: #e5e5e5;")
		self.label_10.setAlignment(Qt.AlignCenter)
		self.label_11 = QLabel(self.homepage)
		self.label_11.setObjectName(u"label_11")
		self.label_11.setGeometry(QRect(80, 70, 841, 311))
		self.label_11.setStyleSheet(u"border: 0.8px solid rgb(85,170,255);")
		self.lineEdit_5 = QLineEdit(self.homepage)
		self.lineEdit_5.setObjectName(u"lineEdit_5")
		self.lineEdit_5.setGeometry(QRect(250, 470, 331, 31))
		font3 = QFont()
		font3.setFamily(u"EB Garamond Medium")
		font3.setPointSize(11)
		self.lineEdit_5.setFont(font3)
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
		self.btnBrowse = QPushButton(self.homepage)
		self.btnBrowse.setObjectName(u"btnBrowse")
		self.btnBrowse.setGeometry(QRect(600, 470, 111, 31))
		font4 = QFont()
		font4.setFamily(u"EB Garamond Medium")
		font4.setPointSize(12)
		self.btnBrowse.setFont(font4)
		self.btnBrowse.setCursor(QCursor(Qt.PointingHandCursor))
		self.btnBrowse.setStyleSheet(u"QPushButton {\n"
"	color:#e5e5e5;\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
		self.btnScan = QPushButton(self.homepage)
		self.btnScan.setObjectName(u"btnScan")
		self.btnScan.setGeometry(QRect(440, 520, 111, 31))
		self.btnScan.setFont(font4)
		self.btnScan.setCursor(QCursor(Qt.PointingHandCursor))
		self.btnScan.setStyleSheet(u"QPushButton {\n"
"	color:#e5e5e5;\n"
"	background-color: rgba(35, 35, 35,0);\n"
"	border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
		self.loadingLabel = QLabel(self.homepage)
		self.loadingLabel.setObjectName(u"loadingLabel")
		self.loadingLabel.setGeometry(QRect(500, 400, 50, 50))
		self.loadingLabel.setMinimumSize(QSize(50, 50))
		self.loadingLabel.setMaximumSize(QSize(50, 50))
		self.stackedWidget.addWidget(self.homepage)
		self.cars = QWidget()
		self.cars.setObjectName(u"cars")
		self.tableWidget = QTableWidget(self.cars)
		if (self.tableWidget.columnCount() < 7):
			self.tableWidget.setColumnCount(7)
		font5 = QFont()
		font5.setFamily(u"EB Garamond")
		font5.setPointSize(12)
		font5.setBold(True)
		font5.setItalic(False)
		font5.setWeight(75)
		__qtablewidgetitem = QTableWidgetItem()
		__qtablewidgetitem.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		__qtablewidgetitem1.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		__qtablewidgetitem2.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
		__qtablewidgetitem3 = QTableWidgetItem()
		__qtablewidgetitem3.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
		__qtablewidgetitem4 = QTableWidgetItem()
		__qtablewidgetitem4.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
		__qtablewidgetitem5 = QTableWidgetItem()
		__qtablewidgetitem5.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
		__qtablewidgetitem6 = QTableWidgetItem()
		__qtablewidgetitem6.setFont(font5);
		self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
		self.tableWidget.setObjectName(u"tableWidget")
		self.tableWidget.setGeometry(QRect(50, 120, 891, 311))
		self.tableWidget.setFont(font4)
		self.tableWidget.setStyleSheet(u"color:#fff")
		self.btnDelete = QPushButton(self.cars)
		self.btnDelete.setObjectName(u"btnDelete")
		self.btnDelete.setGeometry(QRect(430, 480, 111, 31))
		font6 = QFont()
		font6.setFamily(u"EB Garamond Medium")
		font6.setPointSize(14)
		self.btnDelete.setFont(font6)
		self.btnDelete.setCursor(QCursor(Qt.PointingHandCursor))
		self.btnDelete.setStyleSheet(u"background-color:red;\n"
"border-radius: 8px;\n"
"color: #fff;\n"
"outline:none;\n"
"")
		self.label_9 = QLabel(self.cars)
		self.label_9.setObjectName(u"label_9")
		self.label_9.setGeometry(QRect(240, 50, 481, 31))
		self.label_9.setFont(font2)
		self.label_9.setStyleSheet(u"color: #e5e5e5;")
		self.label_9.setAlignment(Qt.AlignCenter)
		self.stackedWidget.addWidget(self.cars)
		self.new_car = QWidget()
		self.new_car.setObjectName(u"new_car")
		self.label = QLabel(self.new_car)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(360, 50, 201, 41))
		self.label.setFont(font2)
		self.label.setStyleSheet(u"color:#fff")
		self.label.setAlignment(Qt.AlignCenter)
		self.groupBox = QGroupBox(self.new_car)
		self.groupBox.setObjectName(u"groupBox")
		self.groupBox.setGeometry(QRect(100, 120, 381, 221))
		self.groupBox.setFont(font6)
		self.groupBox.setStyleSheet(u"color:#fff")
		self.label_2 = QLabel(self.groupBox)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(40, 60, 81, 16))
		self.label_2.setFont(font4)
		self.lineEdit = QLineEdit(self.groupBox)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setGeometry(QRect(140, 60, 181, 31))
		self.lineEdit.setFont(font4)
		self.lineEdit_2 = QLineEdit(self.groupBox)
		self.lineEdit_2.setObjectName(u"lineEdit_2")
		self.lineEdit_2.setGeometry(QRect(140, 110, 181, 31))
		self.lineEdit_2.setFont(font4)
		self.lineEdit_3 = QLineEdit(self.groupBox)
		self.lineEdit_3.setObjectName(u"lineEdit_3")
		self.lineEdit_3.setGeometry(QRect(140, 160, 181, 31))
		self.lineEdit_3.setFont(font4)
		self.label_3 = QLabel(self.groupBox)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setGeometry(QRect(40, 110, 91, 16))
		self.label_3.setFont(font4)
		self.label_4 = QLabel(self.groupBox)
		self.label_4.setObjectName(u"label_4")
		self.label_4.setGeometry(QRect(40, 160, 47, 13))
		self.label_4.setFont(font4)
		self.groupBox_2 = QGroupBox(self.new_car)
		self.groupBox_2.setObjectName(u"groupBox_2")
		self.groupBox_2.setGeometry(QRect(520, 120, 381, 221))
		self.groupBox_2.setFont(font6)
		self.groupBox_2.setStyleSheet(u"color:#fff")
		self.label_5 = QLabel(self.groupBox_2)
		self.label_5.setObjectName(u"label_5")
		self.label_5.setGeometry(QRect(30, 60, 71, 16))
		self.label_5.setFont(font4)
		self.lineEdit_4 = QLineEdit(self.groupBox_2)
		self.lineEdit_4.setObjectName(u"lineEdit_4")
		self.lineEdit_4.setGeometry(QRect(140, 60, 181, 31))
		self.lineEdit_4.setFont(font4)
		self.label_6 = QLabel(self.groupBox_2)
		self.label_6.setObjectName(u"label_6")
		self.label_6.setGeometry(QRect(30, 110, 61, 16))
		self.label_6.setFont(font4)
		self.label_7 = QLabel(self.groupBox_2)
		self.label_7.setObjectName(u"label_7")
		self.label_7.setGeometry(QRect(30, 160, 71, 16))
		self.label_7.setFont(font4)
		self.lineEdit_6 = QLineEdit(self.groupBox_2)
		self.lineEdit_6.setObjectName(u"lineEdit_6")
		self.lineEdit_6.setGeometry(QRect(140, 160, 181, 31))
		self.lineEdit_6.setFont(font4)
		self.comboBox_2 = QComboBox(self.groupBox_2)
		self.comboBox_2.setObjectName(u"comboBox_2")
		self.comboBox_2.setGeometry(QRect(140, 110, 181, 31))
		self.comboBox_2.setFont(font4)
		self.comboBox_2.setFrame(True)
		self.label_8 = QLabel(self.new_car)
		self.label_8.setObjectName(u"label_8")
		self.label_8.setGeometry(QRect(240, 370, 111, 21))
		self.label_8.setFont(font4)
		self.label_8.setStyleSheet(u"color:#fff;")
		self.comboBox = QComboBox(self.new_car)
		self.comboBox.setObjectName(u"comboBox")
		self.comboBox.setGeometry(QRect(370, 370, 201, 31))
		self.comboBox.setFont(font4)
		self.comboBox.setStyleSheet(u"color: #fff;")
		self.btnSave = QPushButton(self.new_car)
		self.btnSave.setObjectName(u"btnSave")
		self.btnSave.setGeometry(QRect(420, 460, 111, 31))
		self.btnSave.setFont(font6)
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

		self.stackedWidget.setCurrentIndex(0)


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
		self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
		self.btnScan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
		self.loadingLabel.setText("")
		___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
		___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"License_Plate", None));
		___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
		___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Vehicle_make", None));
		___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
		___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Vehicle Model", None));
		___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
		___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Id_Number", None));
		___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
		___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Position", None));
		___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
		___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Full_Name", None));
		___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
		___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Parking_Area", None));
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

		self.positions = ['Lecturer', 'Staff']
		self.comboBox_2.addItems(self.positions)

		self.posts = ["Lecturers Bay", "Staff Bay"]
		self.comboBox.addItems(self.posts)

		self.tableWidget.setColumnWidth(5, 220)
		self.tableWidget.setColumnWidth(6, 150)

		self.stylesheet = stylesheet = "::section{color: #333;}"
		self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
	# retranslateUi

