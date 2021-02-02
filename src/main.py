from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import time


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # by default a Pomodoro has 4 blocks of work and in each block there are different stages
        # like Pomodoro (working time) short-break (short rest) and long break (long rest)
        self.pomodoroCount = 0
        # Time counter
        self.count = 0
        # Boolean that control if the timer has started or not
        self.start = False

        # Set buttons title
        self.setWindowTitle("Pomodoro Focus")

        # Set central Widget as a MainWindow it must have a Central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # components of the ui
        grid_layout = QGridLayout()
        pomodoro_button = QPushButton("Pomodoro")
        short_break_button = QPushButton("Short Break")
        long_break_button = QPushButton("Long Break")
        place_holder = QLabel("Place Holder")
        place_holder.setStyleSheet("border: 3px solid black")
        place_holder.setFont(QFont("Times", 15))
        start_button = QPushButton("Start")
        settings_button = QPushButton("Settings")
        grid_layout.addWidget(pomodoro_button, 0, 0)
        grid_layout.addWidget(short_break_button, 0, 1)
        grid_layout.addWidget(long_break_button, 0, 2)
        grid_layout.addWidget(place_holder, 1, 1)
        grid_layout.addWidget(start_button, 2, 1)
        grid_layout.addWidget(settings_button, 3, 1)
        self.centralWidget.setLayout(grid_layout)
        # shows all the widgets
        self.show()

    def start_pomodoro(self):
        pass
        # # we set tha flag to true
        # self.start = True
        #
        # # if the count reaches to 0 we set it to false
        # if self.count == 0:
        #     self.start = False

    def pomodoro(self):
        # TODO: write the logic behind the pomodoro technique
        pass

    def short_break(self):
        pass

    def long_break(self):
        pass

    def settings(self):
        # TODO: write the pomodoro configuration options
        pass

    @staticmethod
    def countdown(t):
        # TODO: write the count down method
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1


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
