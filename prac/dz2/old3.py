
#euler_1d некоректна


import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication,QToolBar,QLineEdit,QVBoxLayout,QWidget,QPushButton
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtWidgets import *
from math import sin,cos

def euler_1d(str_fun,symbol,x0,itercount,shag,max_x=1000):
    max_x = int(max_x)
    x = int(x0)
    tochki = [[x,0]]
    for ii in range(itercount):
        if x>max_x: break
        x+= shag*eval(str_fun.replace(symbol,enc(x)).replace("t",enc((ii+1)*shag)))
        tochki.append([x,(ii+1)*shag])
    return tochki

#def euler(str_fun,symbol,x0,itercount,shag):
#    x = x0
#    tochki = [ [x,ii*shag] for ii,elem in x+=shag*eval(str_fun.replace(symbol,enc(x)))]
#    return tochki

def enc(str1):
    if type(str1)!=type("a"):
        try:    str1 = str(str1)
        except: print("enc cant convert to str")
    return "(" + str1 + ")"

def pravayachast1(str_fun):
    a = str_fun.find("=")
    return str_fun[a+1:]

#print(euler_1d("y+1","y",1,10,0.01))
#print(pravayachast1("dy/dx = y+1"))


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        str_fun = "dy/dx = y-(y**3)-0.25*y+0.3*cos(1*t)"
        str_ny = "y0 = 0"
        str_max = "100"
        self.txt_fun = QLineEdit(str_fun)
        self.txt_ny  = QLineEdit(str_ny)
        self.txt_max = QLineEdit(str_max)
        
        self.series = QLineSeries()
        tochki = euler_1d(pravayachast1(str_fun),"y",pravayachast1(str_ny),10000,0.01,str_max)
        print(tochki)
        for elem in tochki:
            self.series.append(elem[1],elem[0])
        
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
        layout.addWidget(self.txt_fun)
        layout.addWidget(self.txt_ny)
        layout.addWidget(self.txt_max)
        layout.addWidget(button1)
        mainwidget = QWidget()
        mainwidget.setLayout(layout)

        self.setCentralWidget(mainwidget)


app = QApplication(sys.argv)

window = TestChart()
window.show()
window.resize(1000, 700)
sys.exit(app.exec())
