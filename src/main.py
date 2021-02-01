from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set window title
        self.setWindowTitle("Pomodoro")

        # Set the size of the window
        self.setMinimumSize(1024, 768)
        self.setMaximumSize(1024, 768)

    # TODO: create the gui interface in which the user sees whats happening

    # TODO: write the logic behind the pomodoro technique

    # TODO: write the count down method

    # TODO: write the pomodoro configuration options

    # TODO: Info button that shows you in the browser what is the Pomodoro technique

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
