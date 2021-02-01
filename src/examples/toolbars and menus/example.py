import sys
from PyQt5.QtWidgets import QApplication, QWidget
# You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app.
# if you know you won't use command line arguments QApplication([]) i.
app = QApplication(sys.argv)

window = QWidget()
window.show() # IMPORTANT!!! Windows are hidden by default.

# Start the event loop
app.exec()