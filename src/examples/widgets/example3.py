from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My awesome app")

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        # For tristate: widgets.setCheckState(Qt.Partiallychecked)
        # or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
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