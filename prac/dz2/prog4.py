import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication,QToolBar,QLineEdit,QVBoxLayout,QWidget,QPushButton
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtWidgets import *
from math import sin,cos
from sympy import Symbol, diff, expand

def euler_1d(str_fun,symbol,x0,itercount,shag,max_x=1000):
    max_x = int(max_x)
    x = int(x0)
    tochki = [[x,0]]
    for ii in range(itercount):
        if x>max_x: break
        x+= shag*eval(str_fun.replace(symbol,enc(x)).replace("t",enc((ii+1)*shag)))
        tochki.append([x,(ii+1)*shag])
    return tochki

def euler(str_fun1,str_fun2,symbol,nachal1nieyclovia,itercount,shag,max_x=1000):
    max_x = float(max_x)
    tochki = [[nachal1nieyclovia[0],nachal1nieyclovia[1]]]
    x = nachal1nieyclovia[0]
    y = nachal1nieyclovia[1]

    for ii in range(itercount):
        if x>max_x or y>max_x:     break
        x += shag * eval(str_fun1.replace("y",enc(y)).replace(symbol,enc(x)).replace("t",enc((1+ii)*shag)))
        y += shag * eval(str_fun2.replace("y",enc(y)).replace(symbol,enc(x)).replace("t",enc((1+ii)*shag)))
        tochki.append([x,y])
    return tochki

def enc(str1):
    if type(str1)!=type("a"):
        try:    str1 = str(str1)
        except: print("enc cant convert to str")
    return "(" + str1 + ")"

def perenosubravnol1(s):
    a = s.find("=")
    if s[a+1]==0:
        return s
    return enc(s[:a])+"-"+enc(s[a+1:])#+"=0"

def ode_to_str_fun_sys(str1,symbol):
    print("ode_to_str_fun_sys start")
    str_fun1 = ""
    str_fun2 = ""
    print(str1)
    str1 = str(expand(perenosubravnol1(str1)))
    print(str1)
    ls = str1.replace("-","+-").split("+")
    print(ls)
#НАДЕЮСЬ ЧТО ПОСЛЕДНИЙ ЕЛЕМ И ЕСТЬ НАИВЫСШАЯ СТЕПЕНЬ ПРОИЗВОДНОЙ ЛОЛ, ПОТОМ НАПИШУ ФУНКЦИИ СОРТИРОВКИ С КЛЮЧЕМ НА ПРОВЕРКУ ВЫСШЕЙ СТЕПЕНИ ПРОИЗВОДНОЙ
#это на основании что был проюсан expand и наибольшее кол-во несокращенных делений в конце строки, ток это не основываясь на документации
    str2 = ""
    for elem in ls[:-1]: str2=str2+"+"+elem
    str2 = str2.replace("+-","~").replace("+","-").replace("~","+")#перенесли все кроме высшей степени dx^n/dnt в правую сторону
    print(str2)
    
    dsymbdt = "d"+symbol+"/dt"
    str2 = str2.replace(dsymbdt,"y")
    print(str2)
    print("ode_to_str_fun_sys end")
    return "y", str2

def pravayachast1(str_fun):
    a = str_fun.find("=")
    return str_fun[a+1:]

class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        str_fun = "d(dx/dt)/dt + 0.25*(dx/dt)-x+x**3 = 0.3*cos(t)"
        str_ny = "x0 = 0, y0 = 0"
        str_max = "100"
        self.str_fun_x,self.str_fun_y = ode_to_str_fun_sys(str_fun,"x")
        print(self.str_fun_x,self.str_fun_y )

        self.txt_fun = QLineEdit(str_fun)
        self.txt_ny  = QLineEdit(str_ny)
        self.txt_max = QLineEdit(str_max)
        
        str_nyl = str_ny.split(",")
        try:
            str_nyl[0] = float(pravayachast1(str_nyl[0]))
            str_nyl[1] = float(pravayachast1(str_nyl[1]))
        except:
            print("c nachal1nimi ycloviyami trabl")
        self.series = QLineSeries()
        tochki = euler(self.str_fun_x,self.str_fun_y ,"x",str_nyl,10000,0.01,str_max)
        #print(tochki)
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
