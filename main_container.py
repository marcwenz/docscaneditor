from PyQt5 import QtWidgets, QtCore
from parts.thumbnailbar import ThumbnailBar
from parts.toolbar import Toolbar
from parts.bottombar import BottomBar
from parts.gridpreview import GridPreview
from parts.largepreview import LargePreview
from utils import generateThumbnail
from os import scandir
from qrscanner import matchQrCode


class MainContainer(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.qrscan = 1
        self.qrinfo = "EWF Intertax"
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

        # TODO rebuild document management and scannig with DocumentManager class
        self.readDocuments()
        self.gridpreview.displayDocument(self.documents[0])

    def populate(self):
        for im in self.documents:
            self.thumbnailbar.addDocument(im)

    def readDocuments(self):
        for im in scandir("scans"):
            if not im.is_file() and im.path.split(".") != "bmp":
                continue
            if self.qrscan:
                if matchQrCode(im.path, self.qrinfo):
                    self.newDocument(im)
                else:
                    if len(self.documents) == 0:
                        self.newDocument(im)
                    else:
                        self.addPage(im)

    def thumbnailClicked(self, th):
        self.gridpreview.displayDocument(self.documents[th.index])

    def genImTuple(self, path):
        return (path, generateThumbnail(path))

    def sizeHint(self):
        return QtCore.QSize(1920, 1080)

    def nd(self):
        self.newDocument(self.genImTuple("1.bmp"))

    def newDocument(self, im):
        im = self.genImTuple(str(im.path))
        self.documents.append([im])
        if len(self.documents) == 1:
            pass
        self.thumbnailbar.addThumbnail(im, len(self.documents) - 1)

    def addPage(self, im):
        im = self.genImTuple(str(im.path))
        self.documents[-1].append(im)

    def appendToDocument(self, im, idx):
        pass
