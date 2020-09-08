from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy
from parts.thumbnailbar import ThumbnailElement


class GridPreview(QtWidgets.QScrollArea):
    maxColumns = 3

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("border: 1px solid black")
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        QtWidgets.QScroller.grabGesture(
            self, QtWidgets.QScroller.LeftMouseButtonGesture)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setMinimumHeight(1080)

        self.widget = QtWidgets.QWidget(self)
        self.setWidget(self.widget)
        self.containerLayout = QtWidgets.QVBoxLayout(self.widget)
        self.hContainer = QtWidgets.QHBoxLayout()
        self.gridLayout = GridHelper(3)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer = QtWidgets.QSpacerItem(0, 0, QSizePolicy.Expanding,
                                       QSizePolicy.Expanding)
        # vSpacer = QtWidgets.QSpacerItem(0, 0, QSizePolicy.Expanding,
        # QSizePolicy.Expanding)

        self.hContainer.addLayout(self.gridLayout)
        self.hContainer.addSpacerItem(spacer)
        self.containerLayout.addLayout(self.hContainer)
        self.containerLayout.addSpacerItem(spacer)

        self.setWidgetResizable(True)

    def displayDocument(self, doc):
        print("Generating new Grid")
        self.gridLayout.clearGrid()
        for im in doc:
            self.gridLayout.addNext(ThumbnailElement(im, width=250))

    def addToDocument(self, im):
        self.gridLayout.addNext(ThumbnailElement(im, width=250))

    def sizeHint(self):
        return QtCore.QSize(900, 900)


class GridHelper(QtWidgets.QGridLayout):
    def __init__(self, maxcol=1):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.ccount = maxcol
        self.row, self.col = 0, 0

    def addNext(self, widget):
        self.addWidget(widget, *self.getNext(), 1, 1)

    def getNext(self):
        c = (self.row, self.col)
        self.col += 1
        if not self.col < self.ccount:
            self.row += 1
            self.col = 0
        return c

    def clearGrid(self):
        self.row, self.col = 0, 0
        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)
