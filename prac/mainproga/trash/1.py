from math import sin,cos
from sympy import Symbol, diff, expand
from pyray import *
import raylib

#===============================================================================================
def euler(strfunc1,strfunc2,x1_0,x2_0,itercount,shag,wWidth):
    tochki = [[x1_0,x2_0]]
    wWidth += 500
    
    x1 = x1_0
    x2 = x2_0
    
    for _ in range(itercount):
        x1, x2 = x1 + shag * eval(strfunc1.replace("x2",enc(x2)).replace("x1",enc(x1))), x2 + shag * eval(strfunc2.replace("x2",enc(x2)).replace("x1",enc(x1)))
        tochki.append([x1,x2])
        if abs(x1) > wWidth or abs(x2) > wWidth:
            break
    return tochki

def alignwithcenter(dotlist,xStart,yStart,mashtab):
    for elem in dotlist:
        elem[0] = xStart + elem[0]*mashtab
        elem[1] = yStart - elem[1]*mashtab
    return dotlist

def perenosubravnol1(s):
    a = s.find("=")
    if s[a+1]==0:        return s
    return s[:a]+"-"+enc(s[a+1:])#+"=0"

#===============================================================================================

def enc(str1):
    if type(str1)!=type("a"):        str1 = str(str1)
    return "(" + str1 + ")"

def str_mul(str1,str2):
    return str1 + "*" + enc(str2)

def reverse_2D_strfun_Matrix(df1x1,df1x2,df2x1,df2x2):#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # [[a b] [c d]] -1  =  1/(ad-bc) [d -b] [-c a]
    #// ad != bc |x1=.. x2=..
    #https://math.stackexchange.com/questions/3835371/does-it-make-sense-to-define-the-inverse-of-a-matrix-of-functions
    str_k = "(-1) /" +enc(enc(df1x1)+"*"+ enc(df2x2)+"-"+enc(df1x2)+"*"+enc(df2x1)) 
    return str_mul(str_k,df2x2),str_mul(str_k,"-"+df1x2),str_mul(str_k,"-"+df2x1),str_mul(str_k,df2x2)

def euler_for_R():#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # F = R( x(a,p),x(b,p) ) ~= 0 <- euler
    pass

def euler_for_MPP():
    pass

def mpp():
    # dp/dt = ( [dF/dt]^-1 ) * F(p0) }
    # p(0) = p0                      } <- MPP
    pass

def bneshn():
    # [dF/dt] = dR/(dx(a,p)) * dx/dp|(a,p) + dR/(dx(b,p)) * dx/dp|(b,p)  } <- BNESHN
    pass

def bnytr():
    # X|(t,p) = dx/dp|(t,p) :  X/dt = f(t,p)  } 
    #                          X|t* = p       } <- BNYTR
    pass

def main():
    #in: f() | p~R | t=[a..b] | t*<-[a,b]
    
    pass