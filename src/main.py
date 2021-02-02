from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import time


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # by default a Pomodoro has 4 blocks of work
        self.pomodoroCount = 4
        self.pomodoro_stage = ""
        # count down thingy
        self.count = 0
        # Boolean that control if the timer has started or not
        self.start = False

        # Set window title
        self.setWindowTitle("Pomodoro Focus")

        # Set the size of the window
        # self.setGeometry(100, 100, 400, 600)

        # components of the ui
        self.user_ui()

        # shows all the widgets
        self.show()

    def user_ui(self):
        # we declare the buttons
        pomodoro_button = QPushButton("Pomodoro", self)
        short_break_button = QPushButton("Short-Break", self)
        long_break_button = QPushButton("Long_break", self)
        start_button = QPushButton("Start", self)
        settings = QPushButton("Settings", self)

        # we create the label timer
        time_label = QLabel("Place-Holder", self)
        time_label.setStyleSheet("border: 3px solid black")
        time_label.setFont(QFont('times', 15))
        time_label.setAlignment(Qt.AlignCenter)

        # we add the buttons to the grid layout
        grid = QGridLayout()
        grid.addWidget(pomodoro_button, 0, 0)
        grid.addWidget(short_break_button, 0, 1)
        grid.addWidget(long_break_button, 0, 2)
        grid.addWidget(start_button, 2, 1)
        grid.addWidget(settings, 3, 1)
        grid.addWidget(time_label, 1, 1)

        # we add functionality to the buttons
        pomodoro_button.clicked.connect(self.pomodoro)
        short_break_button.clicked.connect(self.short_break)
        long_break_button.clicked.connect(self.long_break)
        start_button.clicked.connect(self.start_pomodoro)
        settings.clicked.connect(self.settings)



        # we add it to the grid layout


        # main_layout = QHBoxLayout()

        # main_layout.addWidget(QPushButton("Pomodoro"))
        # main_layout.addWidget(QPushButton("Short break"))
        # main_layout.addWidget(QPushButton("Long Break"))

        # widget = QWidget()
        # widget.setLayout(main_layout)
        # widget.setGeometry(125, 100, 150, 50)

        # layout = QGridLayout()
        # layout.addWidget(QPushButton("Pomodoro"), 0, 0)
        # layout.addWidget(QPushButton("Short-break"), 0, 1)
        # layout.addWidget(QPushButton("Long-break"), 0, 2)
        #
        # widget = QWidget()
        # widget.setLayout(layout)

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
# window.show()  # IMPORTANT !!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your Application won't reach here until you exit and the event
# loop has stopped
