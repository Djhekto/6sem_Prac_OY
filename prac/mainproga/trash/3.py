#peredelat1 main nado

import sys
from math import sin,cos
from sympy import Symbol, diff, expand
from pyray import *
import raylib

def enc(str1):
    if type(str1)!=type("a"):        str1 = str(str1)
    return "(" + str1 + ")"

def str_mul(str1,str2):
    return str1 + "*" + enc(str2)

def reverse_2D_strfun_Matrix(df1x1,df1x2,df2x1,df2x2):
    # [[a b] [c d]] -1  =  1/(ad-bc) [d -b] [-c a]
    #// ad != bc |x1=.. x2=..
    #https://math.stackexchange.com/questions/3835371/does-it-make-sense-to-define-the-inverse-of-a-matrix-of-functions
    str_k = "(-1) /" +enc(enc(df1x1)+"*"+ enc(df2x2)+"-"+enc(df1x2)+"*"+enc(df2x1)) 
    return str_mul(str_k,df2x2),str_mul(str_k,"-"+df1x2),str_mul(str_k,"-"+df2x1),str_mul(str_k,df2x2)

def pravayachast1(s):
    a = s.find("=")
    if a==-1:        return s
    return s[a+1:]

def euler_for_R(tz,a,b):#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pass

def trytogetridofquestions(symbols,symbols_with_clear_ab,yslovia,strf1,strf2,strf3,strf4,a,b):
    print(symbols,symbols_with_clear_ab,yslovia,strf1,strf2,strf3,strf4)
    strflist = [strf1,strf2,strf3,strf4]
    yslovia1 = yslovia
    ii = 0
    for i,elem in enumerate(symbols):
        if elem not in symbols_with_clear_ab:
            print(elem)
            yslovia1[ii]  = strflist[i].replace("t",enc(a))
            #for bykva in symbols_with_clear_ab:
            #    yslovia1[ii] = yslovia1[ii].replace(bykva,)
            yslovia1[ii+1]= strflist[i].replace("t",enc(b))
        ii+=2    
    return yslovia1

def main():
    fullinput = sys.stdin.readlines()
    for ii,elem in enumerate(fullinput):
        fullinput[ii] = pravayachast1(elem.replace(" =","=").replace("= ","=").replace("\n","").replace("^","**"))
    print(fullinput)
    strf1 = fullinput[0]
    strf2 = fullinput[1]
    strf3 = fullinput[2]
    strf4 = fullinput[3]
    print("syst\n",strf1,strf2,strf3,strf4,sep="  ,  ")
    yslovia = fullinput[4:11+1]
    print(yslovia)
    a,b = eval(fullinput[12])
    print("time\n",a,b)
    tz = fullinput[13]
    print("t*=",tz)
    x1p,x2p,x3p,x4p = eval(fullinput[14])
    print("guess","x1 ",x1p,"  x2 ",x2p,"  x3 ",x3p,"  x4 ",x4p)
    symbols = []
    for elem in fullinput[15].split(","):
        symbols.append(elem)
    print("symbols",symbols)
    symbols_with_clear_ab = []
    if yslovia[0]!="?" and yslovia[1]!="?": symbols_with_clear_ab.append(symbols[0])
    if yslovia[2]!="?" and yslovia[3]!="?": symbols_with_clear_ab.append(symbols[1])
    if yslovia[4]!="?" and yslovia[5]!="?": symbols_with_clear_ab.append(symbols[2])
    if yslovia[6]!="?" and yslovia[7]!="?": symbols_with_clear_ab.append(symbols[3])
    print("s ab",symbols_with_clear_ab)
    yslovia = trytogetridofquestions(symbols,symbols_with_clear_ab,yslovia,strf1,strf2,strf3,strf4,a,b)
    print(yslovia)
    
    return

main()