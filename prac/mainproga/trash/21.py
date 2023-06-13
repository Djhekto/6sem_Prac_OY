#derived from gpt4 with web access
#cant find the src :(

import sys
from PyQt6 import QtWidgets
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create a QWidget to hold the plots
        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)

        # Create a layout for the QWidget
        layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(layout)

        # Create the first plot
        self.plot1 = pg.PlotWidget()
        self.plot1.plot([1, 2, 3, 4, 5], [30, 32, 34, 32, 33])
        layout.addWidget(self.plot1)

        # Create the second plot
        self.plot2 = pg.PlotWidget()
        self.plot2.plot([1, 2, 3, 4, 5], [29, 32, 35, 45, 50])
        layout.addWidget(self.plot2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()