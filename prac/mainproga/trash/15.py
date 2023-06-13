"""
>>> from sympy import Symbol, diff, expand, Matrix,eye
>>> a =  Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [3*x1**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 3*x1*x2/(x1**2 + x2**2)**(5/2), 0, 0], [3*x1*x2/(x1**2 + x2**2)**(5/2), 3*x2**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 0, 0]])
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'x1' is not defined  
>>> x1 = Symbol("x1") 
>>> a =  Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [3*x1**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 3*x1*x2/(x1**2 + x2**2)**(5/2), 0, 0], [3*x1*x2/(x1**2 + x2**2)**(5/2), 3*x2**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 0, 0]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x2' is not defined. Did you mean: 'x1'?
>>> x2 = Symbol("x2")        
>>> x3 = Symbol("x3") 
>>> x4 = Symbol("x4") 
>>> a =  Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [3*x1**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 3*x1*x2/(x1**2 + x2**2)**(5/2), 1, 0], [3*x1*x2/(x1**2 + x2**2)**(5/2), 3*x2**2/(x1**2 + x2**2)**(5/2) - 1/(x1**2 + x2**2)**(3/2), 0, 1]])
>>> a.inv()            
Matrix([
[                                                                          1,                                                                           0, 0, 0],
[                                                                          0,                                                                           1, 0, 0],
[(-3*x1**2*(x1**2 + x2**2)**1.5 + (x1**2 + x2**2)**2.5)/(x1**2 + x2**2)**4.0,                                               -3*x1*x2/(x1**2 + x2**2)**2.5, 1, 0],
[                                              -3*x1*x2/(x1**2 + x2**2)**2.5, (-3*x2**2*(x1**2 + x2**2)**1.5 + (x1**2 + x2**2)**2.5)/(x1**2 + x2**2)**4.0, 0, 1]])
"""

import sys
from math import sin,cos,sqrt
from sympy import Symbol, diff, expand, Matrix,eye

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

def trytoevalyslovia(yslovia):
    for i,list1 in enumerate(yslovia):
        for ii,elem in enumerate(list1):
            yslovia[i][ii] = eval(elem)
    return yslovia

def euler4D_twodirections_returntwo(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.01):
    list4d_tocki_vlevo = []
    list4d_tocki_vpravo = []
    list4d_tocki_vlevo.append(ppp)
    list4d_tocki_vpravo.append(ppp)
    
    #print(symbols,yslovia,strfunlist,a,b,tz,ppp,shag)
    
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
#    print(list4d_tocki)
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
    
    for _ in range( int(1/shag) ):
            
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

def main():
    fullinput = sys.stdin.readlines()
    for ii,elem in enumerate(fullinput):
        fullinput[ii] = pravayachast1(elem.replace(" =","=").replace("= ","=").replace("\n","").replace("^","**"))
    print(fullinput)
    strfunlist = fullinput[0:3+1]
    print("syst\n",strfunlist,sep="  ,  ")
    yslovia = [fullinput[4:6],fullinput[6:8],fullinput[8:10],fullinput[10:12]]
    print(yslovia,"---------------")
    a,b = eval(fullinput[12])
    print("time\n",a,b)
    tz = fullinput[13]
    print("t*=",tz)
    ppp = eval(fullinput[14])
    print("guess",ppp)
    symbols = []
    for ii,elem in enumerate(fullinput[15].split(",")):
        symbols.append([ii,elem])
    print("symbols",symbols)
    yslovia = trytogetridofquestions(symbols,yslovia,strfunlist,a,b)
    print(yslovia,"jdshfkjshdfhksjdhfjkhksdjhfj")
    print(ppp," v ",tz)
    #list4d_tocki = euler4D_twodirections(symbols,yslovia,strfunlist,a,b,tz,ppp)
    #print(list4d_tocki)
    ppp = MPP_4D(symbols,yslovia,strfunlist,a,b,tz,ppp)
    print(ppp)
    
    return

main()