from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro Focus")

        layout = QGridLayout()
        time_label = QLabel("Place-Holder")
        time_label.setStyleSheet("border: 3px solid black")
        time_label.setFont(QFont('times', 15))

        # add widgets to the layout
        layout.addWidget(QPushButton("Pomodoro"), 0, 0)
        layout.addWidget(QPushButton("Short Break"), 0, 1)
        layout.addWidget(QPushButton("Long Break"), 0, 2)
        layout.addWidget(time_label, 1, 1)
        layout.addWidget(QPushButton("Start"), 2, 1)
        layout.addWidget(QPushButton("Settings"), 3, 1)

        # Set the layout ont he application window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())