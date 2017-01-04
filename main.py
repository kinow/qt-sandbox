#!/usr/bin/env python

# NOTE: needs Python 2, for pyqt5

import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)

class Window(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label1.setText("Enter your text")
        input1 = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(input1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        
        
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Window()
    w.resize(530, 140)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())