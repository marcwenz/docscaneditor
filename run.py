import sys

from PyQt5 import QtCore, QtWidgets

from main_container import MainContainer


def run():
    app = QtWidgets.QApplication([])
    gui = MainContainer()
    gui.setWindowTitle("run")
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
