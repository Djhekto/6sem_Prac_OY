import sys
from math import sin,cos,sqrt
from sympy import Symbol, diff, expand, Matrix
from PySide6.QtWidgets import QMainWindow, QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton
from PySide6.QtWidgets import *
import pyqtgraph as pg
import numpy as np
#from pyqtgraph.mkColor import *

def enc(str1):
    if type(str1)!=type("a"):        str1 = str(str1)
    return "(" + str1 + ")"

def str_mul(str1,str2):
    return str1 + "*" + enc(str2)

def pravayachast1(s):
    a = s.find("=")
    if a==-1:        return s
    return s[a+1:]

def trytogetridofquestions(symbols,yslovia,strfunlist,a,b):
    yslovia1 = yslovia
    
    indquest = []
    for i,e in enumerate(yslovia):
        for ii,ee in enumerate(e):
            if ee[0]=="?":
                indquest.append([i,ii])
    
    for [i,ii] in indquest:
        yslovia1[i][ii] = strfunlist[i]

    return yslovia1

def euler4D_twodirections(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.01):
    list4d_tocki_vlevo = []
    list4d_tocki_vpravo = []
    list4d_tocki_vlevo.append(ppp)
    list4d_tocki_vpravo.append(ppp)
    
    print(symbols,yslovia,strfunlist,a,b,tz,ppp,shag)
    
    i=0
    tz_vlevo = eval(tz)
    while tz_vlevo>a:
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vlevo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vlevo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vlevo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vlevo.append(list_append_me)
        tz_vlevo -= shag
        i+=1
        for chislo in list4d_tocki_vlevo[i]:
            if abs(chislo)>=100000:
                tz_vlevo = a
        
    i=0
    tz_vpravo = eval(tz)
    while tz_vpravo<b:
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vpravo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vpravo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vpravo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vpravo.append(list_append_me)
        tz_vpravo += shag
        i+=1
        for chislo in list4d_tocki_vpravo[i]:
            if abs(chislo)>=100000:
                tz_vpravo = b

    list4d_tocki = list(reversed(list4d_tocki_vlevo))[:-1]+list4d_tocki_vpravo
    return list4d_tocki

def euler4D_twodirections_returntwo(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.01):
    list4d_tocki_vlevo = []
    list4d_tocki_vpravo = []
    list4d_tocki_vlevo.append(ppp)
    list4d_tocki_vpravo.append(ppp)
        
    i=0
    tz_vlevo = eval(tz)
    while tz_vlevo>float(a):
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vlevo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vlevo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vlevo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vlevo.append(list_append_me)
        tz_vlevo -= shag
        i+=1
        for chislo in list4d_tocki_vlevo[i]:
            if abs(chislo)>=100000:
                tz_vlevo = a
        
    i=0
    tz_vpravo = eval(tz)
    while tz_vpravo<float(b):
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vpravo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vpravo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vpravo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vpravo.append(list_append_me)
        tz_vpravo += shag
        i+=1
        for chislo in list4d_tocki_vpravo[i]:
            if abs(chislo)>=100000:
                tz_vpravo = b

    list4d_tocki = list(reversed(list4d_tocki_vlevo))[:-1]+list4d_tocki_vpravo
    return list4d_tocki[0],list4d_tocki[-1]

def MPP_4D(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.1):
    ppp1 = ppp
    dx1 = Symbol(symbols[0][1])
    dx2 = Symbol(symbols[1][1])
    dx3 = Symbol(symbols[2][1])
    dx4 = Symbol(symbols[3][1])
    
    Matr_R_0 =  Matrix(1,4,[strfunlist[0],strfunlist[1],strfunlist[2],strfunlist[3]] )    
    for i,e in enumerate(Matr_R_0):
        for ind,symb in symbols:
            Matr_R_0[i] = str(Matr_R_0[i]).replace(symb,enc(ppp[ind]))#p(0)
    Matr_R_0 = Matrix.diag(list(Matr_R_0))
    print(Matr_R_0)  
    
    for _ in range( int(2/shag) ):
            
        vect_koef1 = vnytr_zadacha_4D(symbols,yslovia,strfunlist,a,tz,ppp1)
        vect_koef2 = vnytr_zadacha_4D(symbols,yslovia,strfunlist,b,tz,ppp1)

        Matr_R_a = Matrix(4,4,[
                    str(diff(yslovia[0][0],dx1)),str(diff(yslovia[0][0],dx2)),str(diff(yslovia[0][0],dx3)),str(diff(yslovia[0][0],dx4)),
                    str(diff(yslovia[1][0],dx1)),str(diff(yslovia[1][0],dx2)),str(diff(yslovia[1][0],dx3)),str(diff(yslovia[1][0],dx4)),
                    str(diff(yslovia[2][0],dx1)),str(diff(yslovia[2][0],dx2)),str(diff(yslovia[2][0],dx3)),str(diff(yslovia[2][0],dx4)),
                    str(diff(yslovia[3][0],dx1)),str(diff(yslovia[3][0],dx2)),str(diff(yslovia[3][0],dx3)),str(diff(yslovia[3][0],dx4))]
                    )
        #print("R|a:","\n",Matr_R_a_const,"\n",yslovia)
        Matr_R_b = Matrix(4,4,[
                    str(diff(yslovia[0][1],dx1)),str(diff(yslovia[0][1],dx2)),str(diff(yslovia[0][1],dx3)),str(diff(yslovia[0][1],dx4)),
                    str(diff(yslovia[1][1],dx1)),str(diff(yslovia[1][1],dx2)),str(diff(yslovia[1][1],dx3)),str(diff(yslovia[1][1],dx4)),
                    str(diff(yslovia[2][1],dx1)),str(diff(yslovia[2][1],dx2)),str(diff(yslovia[2][1],dx3)),str(diff(yslovia[2][1],dx4)),
                    str(diff(yslovia[3][1],dx1)),str(diff(yslovia[3][1],dx2)),str(diff(yslovia[3][1],dx3)),str(diff(yslovia[3][1],dx4))]
                    )
        #print("R|b:","\n",Matr_R_b_const,"\n",)  
        
        ppp_a,ppp_b = euler4D_twodirections_returntwo(symbols,yslovia,strfunlist,a,b,tz,ppp1)

        for i,e in enumerate(Matr_R_a):
            for ind,symb in symbols:
                e = str(e).replace(symb,enc(ppp_a[ind]))
            e = e.replace("t",enc(a))
            Matr_R_a[i] = e

        for i,e in enumerate(Matr_R_b):
            for ind,symb in symbols:
                e = str(e).replace(symb,enc(ppp_b[ind]))
            e = e.replace("t",enc(a))
            Matr_R_b[i] = e

        #print("\n",Matr_R_a,Matr_R_b)
            
    #   F'(P) = R'x(a,p)  * dx/dp|(a,p)  +  R'x(b,p)    * dx/dp|(b,p)
        Matr_v1 = Matrix(strfunlist)
        Matr_v2 = Matrix(strfunlist)
        e1 = []
        e2 = []
        for i in range(4):#enumerate(strfunlist):
            e1 = " "+strfunlist[i]
            e2 = " "+strfunlist[i]
            for ind,symb in symbols:
                e1 = e1.replace(symb,enc(vect_koef1[ind]))
                e2 = e2.replace(symb,enc(vect_koef2[ind]))
            e1 = e1.replace("t",enc(a))
            e2 = e2.replace("t",enc(a))
            Matr_v1[i] = expand(e1)
            Matr_v2[i] = expand(e2)
            
        Matr_v1 = Matrix.diag(list(Matr_v1))
        Matr_v2 = Matrix.diag(list(Matr_v2))
        #print(Matr_v1,Matr_v2)    

        Matr_F = Matr_R_a*Matr_v1 + Matr_R_b*Matr_v2
        print(Matr_F)

        try:
            Matr_F.inv()
        except:
            Matr_F = (-1) * Matr_F         
        
        Matr_koef_mpp = (-1)*Matr_F*Matr_R_0
        #print(Matr_koef_mpp)

        iii = 0
        for i in range(4):
            for ii in range(4):
                ppp1[i] = ppp1[i] +  Matr_koef_mpp[iii]
                iii+=1
        print(ppp1)


    return ppp1

def vnytr_zadacha_4D(symbols,yslovia,strfunlist,t,tz,ppp,shag=0.1):
    if float(t)==float(tz): return ppp

    if float(t)<float(tz):#a
        return     euler4D_twodirections_returntwo(symbols,yslovia,strfunlist,t,tz,tz,ppp,shag)[0]
    if float(t)>float(tz):#b
        return     euler4D_twodirections_returntwo(symbols,yslovia,strfunlist,tz,t,tz,ppp,shag)[-1]



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)
        layout = QGridLayout()
        #------------------------------------------------------------------------------------  
        #default input lol
        fullinput = ["dx1/dt = x3","dx2/dt = x4","dx3/dt = -x1 * (x1**2 + x2**2)**(-3/2)","dx4/dt = -x2 * (x1**2 + x2**2)**(-3/2)","x1(a) = 2","x1(b) = 1.0738644361","x2(a) = 0","x2(b) = -1.0995343576","x3(a) =?","x3(b) =?","x4(a) =?","x4(b) =?","t = [0,7]","tz = 0","[2,0,-0.5,0.5]","x1,x2,x3,x4"]
        strfunlist = fullinput[0:3+1]
        yslovia = [fullinput[4:6],fullinput[6:8],fullinput[8:10],fullinput[10:12]]
        t = fullinput[12]
        tz = fullinput[13]
        ppp = fullinput[14]
        symbols = fullinput[15]
        #------------------------------------------------------------------------------------  
        self.txt_fun1 = QLineEdit(strfunlist[0])        
        self.txt_fun2 = QLineEdit(strfunlist[1])        
        self.txt_fun3 = QLineEdit(strfunlist[2])        
        self.txt_fun4 = QLineEdit(strfunlist[3])       
                
        self.txt_y1a = QLineEdit( yslovia[0][0])        
        self.txt_y1b = QLineEdit( yslovia[0][1])        
        self.txt_y2a = QLineEdit( yslovia[1][0])        
        self.txt_y2b = QLineEdit( yslovia[1][1])        
        self.txt_y3a = QLineEdit( yslovia[2][0])        
        self.txt_y3b = QLineEdit( yslovia[2][1])        
        self.txt_y4a = QLineEdit( yslovia[3][0])        
        self.txt_y4b = QLineEdit( yslovia[3][1])        
 
        self.txt_t = QLineEdit(t)        
        self.txt_tz = QLineEdit(tz)        

        self.txt_ppp = QLineEdit(ppp)        
        self.txt_symbols = QLineEdit(symbols)    
        
        self.button1 = QPushButton("push me")
        self.button1.clicked.connect(self.ff1)

        #-------------------------------------------------------------------------------------       
        self.plot1 = pg.PlotWidget()
        #self.plot1.plot([1, 2, 3, 4, 5], [30, 32, 34, 32, 33])
        self.plot1.setBackground("w")
        layout.addWidget(self.plot1,0,0)

        self.plot2 = pg.PlotWidget()
        #self.plot2.plot([1, 2, 3, 4, 5], [29, 32, 35, 45, 50])
        self.plot2.setBackground("w")
        layout.addWidget(self.plot2,0,1)

        self.sup1 = QLabel()
        self.sup1.setText("Система уравнений")
        layout.addWidget(self.sup1,1,0)

        layout.addWidget(self.txt_fun1,2,0)
        layout.addWidget(self.txt_fun2,2,1)
        layout.addWidget(self.txt_fun3,3,0)
        layout.addWidget(self.txt_fun4,3,1)

        self.sup2 = QLabel()
        self.sup2.setText("Краевые условия")
        layout.addWidget(self.sup2,4,0)

        layout.addWidget(self.txt_y1a,5,0)
        layout.addWidget(self.txt_y1b,5,1)
        layout.addWidget(self.txt_y2a,6,0)
        layout.addWidget(self.txt_y2b,6,1)
        layout.addWidget(self.txt_y3a,7,0)
        layout.addWidget(self.txt_y3b,7,1)
        layout.addWidget(self.txt_y4a,8,0)
        layout.addWidget(self.txt_y4b,8,1)

        self.sup3 = QLabel()
        self.sup3.setText("Промежуток времени и время начальной точки")
        layout.addWidget(self.sup3,9,0)
        layout.addWidget(self.txt_t,10,0)
        layout.addWidget(self.txt_tz,10,1)

        self.sup4 = QLabel()
        self.sup4.setText("Вектор указывающий начальную точку и символы используемые в системе")
        layout.addWidget(self.sup4,11,0)
        layout.addWidget(self.txt_ppp,12,0)
        layout.addWidget(self.txt_symbols,12,1)
        
        layout.addWidget(self.button1,13,0)

        self.mainwidget.setLayout(layout)        
        #------------------------------------------------------------------------------------  

    def ff1(self):
        #self.button1.setText("build plot")  

        self.str_fun_list = list(map(pravayachast1,[self.txt_fun1.text(),self.txt_fun2.text(),self.txt_fun3.text(),self.txt_fun4.text()]))

        self.yslovia = [[pravayachast1(self.txt_y1a.text()),pravayachast1(self.txt_y1b.text())],
                        [pravayachast1(self.txt_y2a.text()),pravayachast1(self.txt_y2b.text())],
                        [pravayachast1(self.txt_y3a.text()),pravayachast1(self.txt_y3b.text())],
                        [pravayachast1(self.txt_y4a.text()),pravayachast1(self.txt_y4b.text())]]  

        self.a,self.b = eval(pravayachast1( self.txt_t.text() )) 
        self.tz = pravayachast1(self.txt_tz.text())       
        self.ppp = eval(self.txt_ppp.text())
        self.symbols = []
        for ii,elem in enumerate(self.txt_symbols.text().split(",")):
            self.symbols.append([ii,elem])
        
        self.yslovia = trytogetridofquestions(self.symbols,self.yslovia,self.str_fun_list,self.a,self.b)

        self.list4d_tocki = euler4D_twodirections(self.symbols,self.yslovia,self.str_fun_list,self.a,self.b,self.tz,self.ppp)
        self.ppp_new = MPP_4D(self.symbols,self.yslovia,self.str_fun_list,self.a,self.b,self.tz,self.ppp)
        print(self.ppp_new)
        self.list4d_tocki_new = euler4D_twodirections(self.symbols,self.yslovia,self.str_fun_list,self.a,self.b,self.tz,self.ppp_new)

        for i,_ in enumerate(self.list4d_tocki):
            print(self.list4d_tocki[i],self.list4d_tocki_new[i],"\n")
        
        self.plot1.clear()
        self.plot2.clear()
        self.plot1.showGrid(x=True, y=True, alpha=1.0)
        self.plot2.showGrid(x=True, y=True, alpha=1.0)
        
        temp1_o = pg.PlotDataItem(np.array([a for [a,b,c,d] in self.list4d_tocki[1:]], dtype=float),np.array([b for [a,b,c,d] in self.list4d_tocki[1:]], dtype=float), pen=pg.mkPen('r', width=4), name='old')
        self.plot1.addItem(temp1_o)
        temp2_o = pg.PlotDataItem(np.array([c for [a,b,c,d] in self.list4d_tocki[1:]], dtype=float),np.array([d for [a,b,c,d] in self.list4d_tocki[1:]], dtype=float), pen=pg.mkPen('r', width=4), name='old')
        self.plot2.addItem(temp2_o)
        
#        kostil1_1 = pg.ScatterPlotItem(self.list4d_tocki_new[0][0],self.list4d_tocki_new[0][1], pen=pg.mkPen('b', width=4))
#        self.plot1.addItem(kostil1_1)
        temp1_n = pg.PlotDataItem(np.array([a for [a,b,c,d] in self.list4d_tocki_new[1:]], dtype=float),np.array([b for [a,b,c,d] in self.list4d_tocki_new[1:]], dtype=float), pen=pg.mkPen('b', width=4), name='new')
        self.plot1.addItem(temp1_n)
        
#        kostil1_2 = pg.ScatterPlotItem(self.list4d_tocki_new[0][2],self.list4d_tocki_new[0][3], pen=pg.mkPen('b', width=4))
#        self.plot2.addItem(kostil1_2)
        temp2_n = pg.PlotDataItem(np.array([c for [a,b,c,d] in self.list4d_tocki_new[1:]], dtype=float),np.array([d for [a,b,c,d] in self.list4d_tocki_new[1:]], dtype=float), pen=pg.mkPen('b', width=4), name='new')
        self.plot2.addItem(temp2_n)        
        
        print(self.str_fun_list,self.yslovia ,self.a,self.b,self.tz,self.ppp,self.symbols)


def main():    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.resize(1340, 740)
    sys.exit(app.exec())
    
    return


main()