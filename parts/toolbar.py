from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy

class Toolbar(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setStyleSheet("border: 1px solid black")
        self.button = QtWidgets.QLabel("test", self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.setMinimumSize(100, 100)

    def sizeHint(self):
        return QtCore.QSize(100, 900)
