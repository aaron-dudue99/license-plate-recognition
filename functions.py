from PySide2.QtCore import QObject
from PySide2.QtWidgets import QFileDialog
from ui_main import *


def tr(self, text):
    return QObject.tr(self, text)

# def browseFiles(self):
# 	filename = QFileDialog.getOpenFileName(self,'Open Image',"C:")
# 	fileName = QFileDialog.getOpenFileName(self, self.tr("Open Image"), "C:", self.tr("Image Files (*.png *.jpg *.bmp)"))


def browseFiles(self):
        path_to_file= QFileDialog.getOpenFileName(self, tr("Load Image"), tr("C:"),tr("Images (*.jpg)"))

        self.image_viewer = ImageViewer(path_to_file)
        self.image_viewer.show()


