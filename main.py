import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# imports
from ui_main import Ui_MainWindow
import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils
import easyocr
import mysql.connector as mc
from login import *;

mydb = mc.connect(
    host="localhost",
    user="root",
    passwd="@ADS5188y",
    database="license_plate_rec"
)
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

		#instance variables
		self.imageToScan = ""
		self.scannedNum = ""

		#binding buttons to functions
		self.ui.btnBrowse.clicked.connect(self.showImage)
		self.ui.btnScan.clicked.connect(self.scanPlate)

	def show_popup(self,message,title,status):
		msgBox = QMessageBox()
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		
		if status == "Failed":
			msgBox.setIcon(QMessageBox.Critical)
			msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)

		elif status == "Success":
			msgBox.setIcon(QMessageBox.Information)

		elif status == "Question":
			msgBox.setIcon(QMessageBox.Question)
			msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		ret = msgBox.exec_()
		

	def tr(self, text):
		return QObject.tr(self, text)

	def showImage(self):
		path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load Image"), self.tr("~/"), self.tr("Image Files (*.png *.jpg *.bmp)"))
		self.imageToScan = path_to_file
		self.ui.lineEdit_5.setText(path_to_file)
		pixmap = QPixmap(path_to_file)
		self.ui.label_11.setPixmap(QPixmap(pixmap))
		# self.resize(pixmap.width(),pixmap.height())

	def searchdb(self,platenum):
		print(platenum)
		try:
			mycursor = mydb.cursor()
			query = "SELECT * from vehicles WHERE license_plate = '" + platenum + "'"
			mycursor.execute(query)
			result = mycursor.fetchone()

			if result == None:
				# print('No results For that plate')
				self.show_popup("Plate not in database, Add it Now?", "Add New", "Question")

			else:
				print('Car ' + platenum + ' in database')
				print(result)
		except:
			pass

		print('Scanned Num called')

	def scanPlate(self, image):
		image = self.imageToScan

		if image == "":
			self.show_popup("You need to Upload an image First", "Empty Image", "Failed")

		else:
			img = cv2.imread(self.imageToScan)
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
			bfilter = cv2.bilateralFilter(gray,11,17,17)
			edged = cv2.Canny(bfilter,30,200)
			plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))
			keypoints = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			contours = imutils.grab_contours(keypoints)
			contours = sorted(contours, key = cv2.contourArea,reverse=True)[:10]

			location = None
			for contour in contours:
				approx = cv2.approxPolyDP(contour,10,True)
				if len(approx) == 4:
					location = approx
					break
			
			try:
				if location.size == 0:
					Ui_Form.show_popup(Ui_Form,"No Plate Detected, Please use a different image", "no plate", "Failed")
					return

				else:
					mask = np.zeros(gray.shape, np.uint8)
					new_image = cv2.drawContours(mask,[location], 0,255,-1)
					new_image = cv2.bitwise_and(img,img,mask = mask)
					(x,y) = np.where(mask == 255)
					(x1,y1) = (np.min(x), np.min(y))
					(x2,y2) = (np.max(x), np.max(y))
					cropped_image = gray[x1:x2+1, y1:y2+1]
					reader = easyocr.Reader(['en'])
					result = reader.readtext(cropped_image)
					print(result)
					self.scannedNum = result[0][-2]
					print(self.scannedNum)
					self.searchdb(self.scannedNum)

			except Exception as e:
				print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



