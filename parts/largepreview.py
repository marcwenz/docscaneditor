from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy
from PIL.ImageQt import ImageQt

class LargePreview(QtWidgets.QLabel):
    def __init__(self, image, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setStyleSheet("border: 1px solid black;background:red")
        self.button = QtWidgets.QPushButton("add doc", self)
        self.button.clicked.connect(self.addDocument)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def addDocument(self):
        print("added")
        self.parent().nd()
        # qim = ImageQt(im)
        # pix = QtGui.QPixmap.fromImage(qim)
        # self.setPixmap(pix)

    def sizeHint(self):
        return QtCore.QSize(600, 900)
