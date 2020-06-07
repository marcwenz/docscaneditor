from PyQt5 import QtWidgets, QtCore
from parts.thumbnailbar import ThumbnailBar
from parts.toolbar import Toolbar
from parts.bottombar import BottomBar
from parts.gridpreview import GridPreview
from parts.largepreview import LargePreview
from utils import generateThumbnail


class MainContainer(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.documents = []
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)

        self.thumbnailbar = ThumbnailBar(self)
        self.toolbar = Toolbar(self)
        self.bottombar = BottomBar(self)
        self.gridpreview = GridPreview(self)
        self.largepreview = LargePreview(self)

        self.gridLayout.addWidget(self.thumbnailbar, 0, 0, 5, 1)
        self.gridLayout.addWidget(self.largepreview, 0, 1, 4, 2)
        self.gridLayout.addWidget(self.gridpreview, 0, 3, 4, 3)
        self.gridLayout.addWidget(self.bottombar, 4, 1, 1, 5)
        self.gridLayout.addWidget(self.toolbar, 0, 6, 5, 1)

        self.readDocuments()

    def populate(self):
        for im in self.documents:
            self.thumbnailbar.addDocument(im)

    def readDocuments(self):
        self.newDocument(self.genImTuple("1.bmp"))
        self.addPage(self.genImTuple("2.bmp"))
        self.newDocument(self.genImTuple("1.bmp"))
        self.newDocument(self.genImTuple("2.bmp"))
        self.addPage(self.genImTuple("2.bmp"))
        self.newDocument(self.genImTuple("3.bmp"))
        self.addPage(self.genImTuple("2.bmp"))
        self.addPage(self.genImTuple("1.bmp"))

    def genImTuple(self, path):
        return (path, generateThumbnail(path))

    def sizeHint(self):
        return QtCore.QSize(1920, 1080)

    def nd(self):
        self.newDocument(self.genImTuple("1.bmp"))

    def newDocument(self, im):
        self.documents.append([im])
        if len(self.documents) == 1:
            pass
        self.thumbnailbar.addThumbnail(im)

    def addPage(self, im):
        self.documents[-1].append(im)

    def appendToDocument(self, im, idx):
        pass

