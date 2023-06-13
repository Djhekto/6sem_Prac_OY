# ppp_a = euler|a  -//-b

import sys
from math import sin,cos
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

def euler4D_twodirections(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.1):
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

def MPP_4D(symbols,yslovia,strfunlist,a,b,tz,ppp):
    ppp1 = ppp
    dx1 = Symbol(symbols[0][1])
    dx2 = Symbol(symbols[1][1])
    dx3 = Symbol(symbols[2][1])
    dx4 = Symbol(symbols[3][1])
    
#   F'(P) = R'x(a,p)  * dx/dp|(a,p)  +  R'x(b,p)    * dx/dp|(b,p)
    vect_koef1 = vnytr_zadacha_4D(symbols,yslovia,strfunlist,a,tz,ppp)
    vect_koef2 = vnytr_zadacha_4D(symbols,yslovia,strfunlist,b,tz,ppp)
    print(yslovia,"\n",strfunlist)

    Matr_R =  Matrix(4,4,[
                str(diff(strfunlist[0],dx1)),str(diff(strfunlist[0],dx2)),str(diff(strfunlist[0],dx3)),str(diff(strfunlist[0],dx4)),
                str(diff(strfunlist[1],dx1)),str(diff(strfunlist[1],dx2)),str(diff(strfunlist[1],dx3)),str(diff(strfunlist[1],dx4)),
                str(diff(strfunlist[2],dx1)),str(diff(strfunlist[2],dx2)),str(diff(strfunlist[2],dx3)),str(diff(strfunlist[2],dx4)),
                str(diff(strfunlist[3],dx1)),str(diff(strfunlist[3],dx2)),str(diff(strfunlist[3],dx3)),str(diff(strfunlist[3],dx4))]
                )  
    print(Matr_R,ppp1)
    #print(Matr_R.inv())
    
    Matr_R_a = []
    Matr_R_b = []
    ppp_a = ppp1
    ppp_b = ppp1

    for i,e in enumerate(Matr_R):
        temp_a = str(e)
        for ind,symb in symbols:
            temp_a = temp_a.replace(symb,enc(ppp_a[ind]))   
        temp_a = temp_a.replace("t",enc(a))   
        Matr_R_a.append(eval(temp_a))
    Matr_R_a =  Matrix(4,4,Matr_R_a)
    print("\n",Matr_R_a)
    
    #Matr_F = Matr_R_a*vect_koef1 + Matr_R_b*vect_koef2
    #print(Matr_F)
    
    return ppp1

def vnytr_zadacha_4D(symbols,yslovia,strfunlist,t,tz,ppp,shag=0.1):
    ppp1 = ppp
    if float(t)==float(tz): return Matrix.diag(ppp)
    if float(t)>float(tz): return Matrix.diag(ppp1)
    if float(t)<float(tz): return Matrix.diag(ppp1)

def main():
    fullinput = sys.stdin.readlines()
    for ii,elem in enumerate(fullinput):
        fullinput[ii] = pravayachast1(elem.replace(" =","=").replace("= ","=").replace("\n","").replace("^","**"))
    print(fullinput)
    strfunlist = fullinput[0:3+1]
    print("syst\n",strfunlist,sep="  ,  ")
    yslovia = [fullinput[4:6],fullinput[6:8],fullinput[8:10],fullinput[10:12]]
    print(yslovia)
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