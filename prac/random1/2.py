#https://www.pythonguis.com/tutorials/pyqt6-layouts/
#derived from above
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QLineEdit
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        txt1 = QLineEdit(";kfmasknf")
        layout.addWidget(txt1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()