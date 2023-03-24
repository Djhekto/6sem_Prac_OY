# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the linechart example from Qt v5.x"""
#https://doc.qt.io/qtforpython/examples/example_charts__linechart.html
#derived from above

import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication,QToolBar,QLineEdit,QVBoxLayout,QWidget,QPushButton
from PySide6.QtCharts import QChart, QChartView, QLineSeries

class TestChart(QMainWindow):
    #https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.txt1 = QLineEdit("y = 1111111")
        self.txt2 = QLineEdit("y0 = dfjnsdknывдмлдтыдл1")
        
        self.series = QLineSeries()
        tochki = sozdai_mne_tochki()
        for elem in tochki:
            self.series.append(elem[0],elem[1])
        
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        button1 = QPushButton("push me")
        def ff1():
            button1.setText("and then just touch me")

        button1.clicked.connect(ff1)

        layout.addWidget(self._chart_view)
        layout.addWidget(self.txt1)
        layout.addWidget(self.txt2)
        layout.addWidget(button1)
        mainwidget = QWidget()
        mainwidget.setLayout(layout)

        self.setCentralWidget(mainwidget)

def sozdai_mne_tochki():
    tocki = [[]]
    for i in range(10):
        x = i*1.5
        y = i*1.2
        tocki.append([x,y])
    tocki = tocki[1:]
    return tocki


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(1000, 700)
    sys.exit(app.exec())