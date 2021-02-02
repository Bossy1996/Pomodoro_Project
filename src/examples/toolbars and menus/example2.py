import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# Subclass QMainWindow to customise your application's main buttons

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My second try on PyQt5")

        label = QLabel("This is a PyQt5 buttons!")

        # The 'Qt' name space has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the buttons. Widget will expand
        # to take up all the space in the buttons by default
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("your buttom", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("hello")
        dlg.exec_()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
