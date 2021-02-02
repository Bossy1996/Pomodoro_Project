from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import time

class StackedExample(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Contact' )
        self.leftlist.insertItem(1, 'Personal' )

        self.central_widget = QWidget()               # define central widget
        self.setCentralWidget(self.central_widget)    # set QMainWindow.centralWidget

        self.stack1 = QWidget()
        self.stack2 = QWidget()

        self.stack1UI()
        self.stack2UI()

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)
        self.Stack.addWidget (self.stack2)
        grid = QGridLayout()
        self.centralWidget().setLayout(grid)          # add the layout to the central widget
        grid.addWidget(self.leftlist,0,0)
        grid.addWidget(self.Stack,0,1)

        #self.leftlist.currentRowChanged.connect(self.display)
        self.resize(300,100)
        self.show()

app = QApplication(sys.argv)

window = StackedExample()

app.exec()