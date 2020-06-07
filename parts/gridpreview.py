from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy
from parts.thumbnailbar import ThumbnailElement

class GridPreview(QtWidgets.QScrollArea):
    maxColumns = 3
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("border: 1px solid black")
        self.widget = QtWidgets.QWidget(self)
        self.gridLayout = GridHelper(self.widget)

    def displayDocument(self, doc):
        self.gridLayout.clearGrid()
        for im in doc:
            self.gridLayout.addNext(ThumbnailElement(im[1], width=300))

    def addToDocument(self, im):
        self.gridLayout.addNext(ThumbnailElement(im[1], width=300))

    def sizeHint(self):
        return QtCore.QSize(100, 900)


class GridHelper(QtWidgets.QGridLayout):
    def __init__(self, maxcol=1, parent=None):
        super().__init__(parent=parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.count = maxcol
        self.row = 0
        self.col = 0

    def addNext(self, widget):
        self.addWidget(widget, *self.getNext(), 1, 1)

    def getNext(self):
        c = (self.row, self.col)
        self.col += 1
        if not self.col < self.maxColumns:
            self.row += 1
            self.col = 0
        return c

    def clearGrid(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
