from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import  *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My awesome app")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        # In QListWidget there are two separate signals for the item and the str
        widget.currentItemChanged.connect( self.index_changed )
        widget.currentItemChanged.connect( self.text_changed )

        self.setCentralWidget(widget)

    def index_changed(self, i): # Not an index, i is a QList item
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)


# You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT !!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your Application won't reach here until you exit and the event
# loop has stopped
