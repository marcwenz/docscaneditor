from PyQt5 import QtWidgets, QtCore
from main_container import MainContainer
import sys

def run():
    app = QtWidgets.QApplication([])
    gui = MainContainer()
    gui.setWindowTitle("run")
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
