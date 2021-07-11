import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# imports
from ui_main import Ui_MainWindow
from functions import *

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

		#binding buttons to functions
		self.ui.btnBrowse.clicked.connect(self.showImage)

	def tr(self, text):
		return QObject.tr(self, text)

	def showImage(self):
		path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load Image"), self.tr("~/"), self.tr("Image Files (*.png *.jpg *.bmp)"))
		self.ui.lineEdit_5.setText(path_to_file)
		pixmap = QPixmap(path_to_file)
		self.ui.label_11.setPixmap(QPixmap(pixmap))
		self.resize(pixmap.width(),pixmap.height())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



