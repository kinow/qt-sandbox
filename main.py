#!/usr/bin/env python

# NOTE: needs Python 2, for pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

class Window(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        input1 = QLineEdit()

        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Window()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())