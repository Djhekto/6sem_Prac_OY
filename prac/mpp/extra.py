from math import sin,cos
from sympy import integrate, Symbol, diff, expand
import numpy as np
from pyray import *

def perenosubravnol1(s):
    a = s.find("=")
    if s[a+1]==0:
        return s
    return s[:a]+"-"+s[a+1:]#+"=0"

def enc(str1):
    return "(" + str1 + ")"

def main():
    f1 = input().replace("= ","=")
    f2 = input().replace("= ","=")
    X0 = list(eval(input()))
    f1 = perenosubravnol1(f1).replace(" ","").replace("^","**")
    f2 = perenosubravnol1(f2).replace(" ","").replace("^","**")
    print(f1,f2,X0)

    dx1 = Symbol("x1")
    dx2 = Symbol("x2")

    df1x1 = str(diff(f1,dx1))
    df1x2 = str(diff(f1,dx2))
    df2x1 = str(diff(f2,dx1))
    df2x2 = str(diff(f2,dx2))
    print(df1x1,df1x2,df2x1,df2x2)

    # [[a b] [c d]] -1  =  1/(ab-cd) [d -b] [-c a]
    #? ad != bc
    const_koef = "(-1) /" +enc(enc(df1x1)+"*"+ enc(df2x2)+"-"+enc(df1x2)+"*"+enc(df2x1))
    print(const_koef,expand(const_koef),sep = "  =>  ")
    const_koef = str(expand(const_koef))
    
    f1x1 = enc(const_koef)+"*"+df1x1
    f1x2 = enc(const_koef)+"*"+df1x2
    f2x1 = enc(const_koef)+"*"+df2x1
    f2x2 = enc(const_koef)+"*"+df2x2
    print(f1x1,f1x2,f2x1,f2x2)
    
    constx1 = str(expand( enc(f1x1) +"+"+enc(f1x2) ))
    constx2 = str(expand( enc(f2x1) +"+"+enc(f2x2) ))
    print(constx1,"        ",constx2)
    
    constf1 = f1
    constf2 = f2
    print(constf1,constf2)

    x1_ = X0[0]
    x2_ = X0[1]
    print(x1_,x2_)

    #raylib.DrawLine(startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color)



    wWidth = 1200
    wHeight = 800
    xStart = int(wWidth/2)
    yStart = int(wHeight/2)

    init_window(wWidth, wHeight, "Hello")
    rl.SetTargetFPS(60)
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        
        draw_text("Hello world", 190, 200, 20, VIOLET)
        raylib.rlSetLineWidth(2)

        raylib.DrawLine(0,yStart,wWidth,yStart,BLACK);
        raylib.DrawLine(xStart,0,xStart,wHeight,BLACK);
        raylib.DrawLineStrip([(100,100),(200,200),(150,500)], 3, GRAY)
        
        end_drawing()
    close_window()


from time import time
start_time = time()
main()
print("--- %s seconds ---" % (time() - start_time))