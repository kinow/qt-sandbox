#!/usr/bin/env python

# NOTE: needs Python 2, for pyqt5

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QMenu, QWidgetAction, QApplication)

class PopupAction(QWidgetAction):

    def __init__(self, parent):
        super(QWidgetAction, self).__init__(parent)
        widget = QWidget()
        label1 = QLabel()
        input1 = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(input1)
        widget.setLayout(hbox)
        self.setDefaultWidget(widget)

class PopupMenu(QMenu):

    def __init__(self):
        super(QMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.addAction(PopupAction(self))

    def display(self):
        print("Displaying....")

class Window(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label1.setText("Enter your text")

        input1 = QLineEdit()

        button1 = QPushButton("Show menu")

        popup = PopupMenu()
        button1.setMenu(popup)

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(input1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(button1)
        
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

    def addInputBox(self):
        print("OI")
        pass


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Window()
    w.resize(530, 140)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())