# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color:#14213D;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("b")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: #14213D;")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setEnabled(False)
        self.frame_top.setStyleSheet("background-color:rgba(255,255,255,0)")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgba(35, 35, 35,0);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnHome = QtWidgets.QPushButton(self.frame_top_menus)
        self.btnHome.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnHome.setFont(font)
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHome.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(35, 35, 35,0);\n"
"    border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btnHome.setObjectName("btnHome")
        self.verticalLayout_4.addWidget(self.btnHome)
        self.btnCars = QtWidgets.QPushButton(self.frame_top_menus)
        self.btnCars.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnCars.setFont(font)
        self.btnCars.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCars.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(35, 35, 35,0);\n"
"    border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btnCars.setObjectName("btnCars")
        self.verticalLayout_4.addWidget(self.btnCars)
        self.btnNew = QtWidgets.QPushButton(self.frame_top_menus)
        self.btnNew.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnNew.setFont(font)
        self.btnNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNew.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(35, 35, 35,0);\n"
"    border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btnNew.setObjectName("btnNew")
        self.verticalLayout_4.addWidget(self.btnNew)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.label_10 = QtWidgets.QLabel(self.homepage)
        self.label_10.setGeometry(QtCore.QRect(190, 20, 481, 31))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #e5e5e5;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.homepage)
        self.label_11.setGeometry(QtCore.QRect(140, 110, 631, 241))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.homepage)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 390, 331, 21))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: #e5e5e5;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.btnNew_2 = QtWidgets.QPushButton(self.homepage)
        self.btnNew_2.setGeometry(QtCore.QRect(550, 380, 0, 40))
        self.btnNew_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnNew_2.setFont(font)
        self.btnNew_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNew_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(35, 35, 35,0);\n"
"    border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btnNew_2.setObjectName("btnNew_2")
        self.btnDelete_2 = QtWidgets.QPushButton(self.homepage)
        self.btnDelete_2.setGeometry(QtCore.QRect(550, 390, 111, 21))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(12)
        self.btnDelete_2.setFont(font)
        self.btnDelete_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete_2.setStyleSheet("QPushButton {\n"
"    color:#e5e5e5;\n"
"    background-color: rgba(35, 35, 35,0);\n"
"    border: 2px solid rgb(85,170,255);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btnDelete_2.setObjectName("btnDelete_2")
        self.stackedWidget.addWidget(self.homepage)
        self.cars = QtWidgets.QWidget()
        self.cars.setObjectName("cars")
        self.tableWidget = QtWidgets.QTableWidget(self.cars)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 891, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btnView = QtWidgets.QPushButton(self.cars)
        self.btnView.setGeometry(QtCore.QRect(290, 430, 111, 31))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(14)
        self.btnView.setFont(font)
        self.btnView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnView.setStyleSheet("background-color:#fca311;\n"
"border-radius: 8px;\n"
"color: #14213D;\n"
"border:none;\n"
"outline:none;\n"
"")
        self.btnView.setObjectName("btnView")
        self.btnDelete = QtWidgets.QPushButton(self.cars)
        self.btnDelete.setGeometry(QtCore.QRect(500, 430, 111, 31))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(14)
        self.btnDelete.setFont(font)
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete.setStyleSheet("background-color:red;\n"
"border-radius: 8px;\n"
"color: #fff;\n"
"outline:none;\n"
"")
        self.btnDelete.setObjectName("btnDelete")
        self.label_9 = QtWidgets.QLabel(self.cars)
        self.label_9.setGeometry(QtCore.QRect(220, 50, 481, 31))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #e5e5e5;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.cars)
        self.new_car = QtWidgets.QWidget()
        self.new_car.setObjectName("new_car")
        self.label = QtWidgets.QLabel(self.new_car)
        self.label.setGeometry(QtCore.QRect(320, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.new_car)
        self.groupBox.setGeometry(QtCore.QRect(90, 120, 351, 151))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:#fff")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 181, 20))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 181, 20))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 100, 181, 20))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.new_car)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 120, 351, 151))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color:#fff")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 40, 181, 20))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 100, 181, 20))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 70, 181, 22))
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_8 = QtWidgets.QLabel(self.new_car)
        self.label_8.setGeometry(QtCore.QRect(100, 310, 111, 16))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#fff;")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.new_car)
        self.comboBox.setGeometry(QtCore.QRect(230, 310, 201, 22))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.btnSave = QtWidgets.QPushButton(self.new_car)
        self.btnSave.setGeometry(QtCore.QRect(380, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("EB Garamond Medium")
        font.setPointSize(14)
        self.btnSave.setFont(font)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setStyleSheet("background-color:#fca311;\n"
"border-radius: 8px;\n"
"color: #14213D;\n"
"border:none;\n"
"outline:none;\n"
"")
        self.btnSave.setObjectName("btnSave")
        self.stackedWidget.addWidget(self.new_car)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnHome.setText(_translate("MainWindow", "Home"))
        self.btnCars.setText(_translate("MainWindow", "Vehicles"))
        self.btnNew.setText(_translate("MainWindow", "New"))
        self.label_10.setText(_translate("MainWindow", "License PLate Recognition Homepage"))
        self.btnNew_2.setText(_translate("MainWindow", "New"))
        self.btnDelete_2.setText(_translate("MainWindow", "Browse"))
        self.btnView.setText(_translate("MainWindow", "View"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.label_9.setText(_translate("MainWindow", "List of All Cars"))
        self.label.setText(_translate("MainWindow", "Add a New Vehicle"))
        self.groupBox.setTitle(_translate("MainWindow", "Vehicle Details"))
        self.label_2.setText(_translate("MainWindow", "License Plate"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ABC1234"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Toyota"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Hilux GD6"))
        self.label_3.setText(_translate("MainWindow", "Vehicle Make"))
        self.label_4.setText(_translate("MainWindow", "Model"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Owner Details"))
        self.label_5.setText(_translate("MainWindow", "National ID Nu"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "12-12344567A89"))
        self.label_6.setText(_translate("MainWindow", "Position"))
        self.label_7.setText(_translate("MainWindow", "Full Name"))
        self.label_8.setText(_translate("MainWindow", "Parking Area"))
        self.btnSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
