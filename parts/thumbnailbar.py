from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QSizePolicy

class ThumbnailBar(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        QtWidgets.QScroller.grabGesture(
            self, QtWidgets.QScroller.LeftMouseButtonGesture)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setMinimumHeight(1080)
        self.setMinimumWidth(174)

        self.widget = QtWidgets.QWidget(self)
        self.setWidget(self.widget)
        self.containerLayout = QtWidgets.QVBoxLayout(self.widget)
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.vertLayout = QtWidgets.QVBoxLayout()
        self.vertLayout.setContentsMargins(10, 10, 10, 0)
        self.vertLayout.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)

        self.containerLayout.addLayout(self.vertLayout)
        spacer = QtWidgets.QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.containerLayout.addSpacerItem(spacer)

        self.setWidgetResizable(True)

    def addThumbnail(self, im, ix):
        th = ThumbnailElement(im, ix, width=150, parent=self)
        th.mousePressEvent = lambda _: self.propagateClick(th)
        self.vertLayout.addWidget(th)

    def propagateClick(self, th):
        self.parent().thumbnailClicked(th)

class ThumbnailElement(QtWidgets.QLabel):
    def __init__(self, im, ix=None, width=None, height=None, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(im[0])
        self.index = ix

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        if width:
            img = QtGui.QPixmap.fromImage(im[1]).scaledToWidth(width)
        elif height:
            img = QtGui.QPixmap.fromImage(im[1]).scaledToHeight(height)

        self.setPixmap(img)
        self.setStyleSheet("border: 1px solid black; \
                           background-color: transparent")
