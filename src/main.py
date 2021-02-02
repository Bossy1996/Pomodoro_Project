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
        self.place_holder = QLabel("Place Holder")
        self.place_holder.setStyleSheet("border: 3px solid black")
        self.place_holder.setFont(QFont("Times", 15))
        self.place_holder.setAlignment(Qt.AlignCenter)
        self.place_holder.setFixedSize(QSize(125, 80))
        start_button = QPushButton("Start")
        settings_button = QPushButton("Settings")
        grid_layout.addWidget(pomodoro_button, 0, 0)
        grid_layout.addWidget(short_break_button, 0, 1)
        grid_layout.addWidget(long_break_button, 0, 2)
        grid_layout.addWidget(self.place_holder, 1, 1)
        grid_layout.addWidget(start_button, 2, 1)
        grid_layout.addWidget(settings_button, 3, 1)
        self.centralWidget.setLayout(grid_layout)

        # buttons functionality
        pomodoro_button.clicked.connect(self.pomodoro)
        short_break_button.clicked.connect(self.short_break)
        long_break_button.clicked.connect(self.long_break)
        start_button.clicked.connect(self.start_pomodoro)
        settings_button.clicked.connect(self.settings)

        # the timer thing
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(100)

        # shows all the widgets
        self.show()

    def start_pomodoro(self):
        # # we set tha flag to true
        self.start = True
        print(self.start)

    def pomodoro(self):
        # TODO: write the logic behind the pomodoro technique

        self.count = 25

    def short_break(self):
        self.count = 5

    def long_break(self):
        self.count = 15

    def settings(self):
        # TODO: write the pomodoro configuration options
        pass

    def show_time(self):

        mins, secs = divmod(self.count, 60) # TODO: It's shows only the seconds it should calculate mins and secs

        # getting the text from the count
        time_format = '{:02d}:{:02d}'.format(mins, secs)

        # checking if the flag is true
        if self.start:
            # increment the counter
            self.count -= 1
            time.sleep(1)

            # showing text
            # self.place_holder.setText(time_format)

        self.place_holder.setText(time_format)

        # when the time reaches 0 the working time ends and it adds a pomodoro count + 1
        if self.count == 0:
            self.start = False
            self.pomodoroCount += 1


# TODO: Info button that shows you in the browser what is the Pomodoro technique MAYBE!!!


# You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
# window.show()  # IMPORTANT !!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your Application won't reach here until you exit and the event
# loop has stopped
