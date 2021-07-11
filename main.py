import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# imports
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#__pages___

		#home
		self.ui.btnHome.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.homepage))

		#cars
		self.ui.btnCars.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cars))

		#new
		self.ui.btnNew.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_car))

		self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



