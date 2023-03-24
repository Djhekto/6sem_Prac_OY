# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the linechart example from Qt v5.x"""
#https://doc.qt.io/qtforpython/examples/example_charts__linechart.html
#derived from above

import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication,QToolBar,QLineEdit
from PySide6.QtCharts import QChart, QChartView, QLineSeries

class TestChart(QMainWindow):
    #https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html
    def __init__(self):
        super().__init__()

        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)
        self.txt1 = QLineEdit(";kfmasknf")
        self.addWidget(self.txt1)
#        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.PySide6.QtWidgets.QToolBar.addWidget

"""
    def createToolBars(self):
    #https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html
        fileToolBar = addToolBar()
        fileToolBar.addAction(newAct)
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(1000, 700)
    sys.exit(app.exec())