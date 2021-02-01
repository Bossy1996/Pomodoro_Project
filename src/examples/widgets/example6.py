from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My awesome app")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        widget.returnPressed.connect( self.return_pressed )
        widget.selectionChanged.connect( self.selection_changed )
        widget.textChanged.connect( self.text_changed )
        widget.textEdited.connect( self.text_edited )

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return Pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection Changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text Changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited")
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
