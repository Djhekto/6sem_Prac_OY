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
    if type(str1)!=type("a"):
        str1 = str(str1)
    return "(" + str1 + ")"

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

def main():
    wWidth = 1400
    wHeight = 1000
    mashtab = 150
    xStart = int(wWidth/2)
    yStart = int(wHeight/2)
    
    in1 = input().replace("= ","=").replace(" =","=")
    in2 = input().replace("= ","=").replace(" =","=")
    X0 = list(eval(input()))
    f1 = perenosubravnol1(in1).replace(" ","").replace("^","**")
    f2 = perenosubravnol1(in2).replace(" ","").replace("^","**")
    print(f1,f2,X0)

    x1_ = X0[0]
    x2_ = X0[1]
    
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
    
    const_koef1 = eval(f1.replace("x2",enc(x2_)).replace("x1",enc(x1_)))
    const_koef2 = eval(f2.replace("x2",enc(x2_)).replace("x1",enc(x1_)))   
    print(const_koef1,const_koef2)
    
    f1x1 = enc(const_koef)+"*"+enc(df1x1)
    f1x2 = enc(const_koef)+"*"+enc(df1x2)
    f2x1 = enc(const_koef)+"*"+enc(df2x1)
    f2x2 = enc(const_koef)+"*"+enc(df2x2)
    print(f1x1," ; ",f1x2," ; ",f2x1," ; ",f2x2)
    
    constx1 = str(expand( enc(f1x1) +"+"+enc(f1x2) ))
    constx2 = str(expand( enc(f2x1) +"+"+enc(f2x2) ))
    print(constx1,"        ",constx2)
    
    constf1 = f1
    constf2 = f2
    print(constf1,constf2)

#==================================================================================================================
    init_window(wWidth, wHeight, "Hello")
    rl.SetTargetFPS(60)
    t = 0
    small = 0.01
    while not window_should_close():
        begin_drawing()
        x1_ = 1.1 * cos(t)
        x2_ = 0.8 * cos(t+0.1*t)
        t+=0.05
        print(x1_,x2_)
        try:
            drawpink = False
            if in1[:3]=="x2=" and in2[:3]=="x1=":
                drawpink = True
            
            if drawpink:
                drawp = euler(in2[3:].replace("^","**"),in1[3:].replace("^","**"),x1_,x2_,2000,small,wWidth) 
                drawpa = euler(in2[3:].replace("^","**"),in1[3:].replace("^","**"),x1_,x2_,2000,-small,wWidth)
                drawp = alignwithcenter(drawp,xStart,yStart,mashtab)
                drawpa = alignwithcenter(drawpa,xStart,yStart,mashtab)
            
            draw1 = euler(constf1,constf2,x1_,x2_,2000,small,wWidth) 
            draw1a = euler(constf1,constf2,x1_,x2_,2000,-small,wWidth)    
            draw2 = euler(constx1,constx2,x1_,x2_,2000,small,wWidth)    
            draw2a = euler(constx1,constx2,x1_,x2_,2000,-small,wWidth)    
            draw3 = euler(f1x1,f2x2,x1_,x2_,2000,small,wWidth)    
            draw3a = euler(f1x1,f2x2,x1_,x2_,2000,-small,wWidth)    
            draw4 = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,small,wWidth)
            draw4a = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,-small,wWidth)
            draw9 = euler(enc(constx1)+"*"+enc(const_koef1),enc(constx2)+"*"+enc(const_koef2),x1_,x2_,2000,small,wWidth)    
            draw9a = euler(enc(constx1)+"*"+enc(const_koef1),enc(constx2)+"*"+enc(const_koef2),x1_,x2_,2000,-small,wWidth) 
            
            x1_ = x1_*(-1)
            x2_ = x2_*(-1)
            
            if drawpink:
                drawp1 = euler(in2[3:].replace("^","**"),in1[3:].replace("^","**"),x1_,x2_,2000,small,wWidth) 
                drawp1a = euler(in2[3:].replace("^","**"),in1[3:].replace("^","**"),x1_,x2_,2000,-small,wWidth)
                drawp1 = alignwithcenter(drawp1,xStart,yStart,mashtab)
                drawp1a = alignwithcenter(drawp1a,xStart,yStart,mashtab)
            
            draw5 = euler(constf1,constf2,x1_,x2_,2000,small,wWidth)    
            draw5a = euler(constf1,constf2,x1_,x2_,2000,-small,wWidth)    
            draw6 = euler(constx1,constx2,x1_,x2_,2000,small,wWidth)    
            draw6a = euler(constx1,constx2,x1_,x2_,2000,-small,wWidth)    
            draw7 = euler(f1x1,f2x2,x1_,x2_,2000,small,wWidth)    
            draw7a = euler(f1x1,f2x2,x1_,x2_,2000,-small,wWidth)    
            draw8 = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,small,wWidth)   
            draw8a = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,-small,wWidth)   
            draw10 = euler(enc(constx1)+"*"+enc(const_koef1),enc(constx2)+"*"+enc(const_koef2),x1_,x2_,2000,small,wWidth)    
            draw10a = euler(enc(constx1)+"*"+enc(const_koef1),enc(constx2)+"*"+enc(const_koef2),x1_,x2_,2000,-small,wWidth) 
                    
            draw1 = alignwithcenter(draw1,xStart,yStart,mashtab)
            draw1a = alignwithcenter(draw1a,xStart,yStart,mashtab)
            draw2 = alignwithcenter(draw2,xStart,yStart,mashtab)
            draw2a = alignwithcenter(draw2a,xStart,yStart,mashtab)
            draw3 = alignwithcenter(draw3,xStart,yStart,mashtab)
            draw3a = alignwithcenter(draw3a,xStart,yStart,mashtab)
            draw4 = alignwithcenter(draw4,xStart,yStart,mashtab)
            draw4a = alignwithcenter(draw4a,xStart,yStart,mashtab)
            draw5 = alignwithcenter(draw5,xStart,yStart,mashtab)
            draw5a = alignwithcenter(draw5a,xStart,yStart,mashtab)
            draw6 = alignwithcenter(draw6,xStart,yStart,mashtab)
            draw6a = alignwithcenter(draw6a,xStart,yStart,mashtab)
            draw7 = alignwithcenter(draw7,xStart,yStart,mashtab)
            draw7a = alignwithcenter(draw7a,xStart,yStart,mashtab)
            draw8 = alignwithcenter(draw8,xStart,yStart,mashtab)
            draw8a = alignwithcenter(draw8a,xStart,yStart,mashtab)
            draw9 = alignwithcenter(draw9,xStart,yStart,mashtab)
            draw9a = alignwithcenter(draw9a,xStart,yStart,mashtab)
            draw10 = alignwithcenter(draw10,xStart,yStart,mashtab)
            draw10a = alignwithcenter(draw10a,xStart,yStart,mashtab)
            



            clear_background(WHITE)
            raylib.rlSetLineWidth(3)
            
            raylib.DrawLine(0,yStart,wWidth,yStart,BLACK);
            raylib.DrawLine(xStart,0,xStart,wHeight,BLACK);
            raylib.DrawLine(0,yStart+mashtab,wWidth,yStart+mashtab,LIGHTGRAY);
            raylib.DrawLine(0,yStart-mashtab,wWidth,yStart-mashtab,LIGHTGRAY);
            raylib.DrawLine(xStart+mashtab,0,xStart+mashtab,wHeight,LIGHTGRAY);
            raylib.DrawLine(xStart-mashtab,0,xStart-mashtab,wHeight,LIGHTGRAY);
            
            raylib.DrawLineStrip(draw1, len(draw1), BLUE)
            raylib.DrawLineStrip(draw1a, len(draw1a), BLUE)
            raylib.DrawLineStrip(draw9, len(draw9), BROWN)
            raylib.DrawLineStrip(draw9a, len(draw9a), BROWN)
            raylib.DrawLineStrip(draw10, len(draw10), BROWN)
            raylib.DrawLineStrip(draw10a, len(draw10a), BROWN)
            raylib.DrawLineStrip(draw2, len(draw2), RED)
            raylib.DrawLineStrip(draw2a, len(draw2a), RED)
            raylib.DrawLineStrip(draw3, len(draw3), ORANGE)
            raylib.DrawLineStrip(draw3a, len(draw3a), ORANGE)
            raylib.DrawLineStrip(draw4, len(draw4), GREEN)
            raylib.DrawLineStrip(draw4a, len(draw4a), GREEN)
            raylib.DrawLineStrip(draw5, len(draw5), (20, 141, 201, 235))
            raylib.DrawLineStrip(draw5a, len(draw5a), (20, 141, 201, 235))
            raylib.DrawLineStrip(draw6, len(draw6), (230, 41, 55, 200))
            raylib.DrawLineStrip(draw6a, len(draw6a), (230, 41, 55, 200))
            raylib.DrawLineStrip(draw7, len(draw7), (200, 161, 0, 255))
            raylib.DrawLineStrip(draw7a, len(draw7a), (200, 161, 0, 255))
            raylib.DrawLineStrip(draw8, len(draw8), (0, 225, 0, 255))
            raylib.DrawLineStrip(draw8a, len(draw8a), (0, 225, 0, 255))


            if drawpink:
                raylib.DrawLineStrip(drawp, len(drawp), PINK)
                raylib.DrawLineStrip(drawpa, len(drawpa), PINK) 
                raylib.DrawLineStrip(drawp1, len(drawp), PINK)
                raylib.DrawLineStrip(drawp1a, len(drawpa), PINK)                   


            draw_text(in1, wWidth-400, 20, 20, PINK)
            draw_text(in2, wWidth-400, 50, 20, PINK)        
            draw_text(str(X0)+" "+str(tuple([-x for x in X0])), wWidth-400, 80, 20, PINK)        
            draw_text(constf1, wWidth-400, 100, 20, BLUE)
            draw_text(constf2, wWidth-400, 130, 20, BLUE)
            draw_text(constx1, wWidth-400, 170, 20, RED)
            draw_text(constx2, wWidth-400, 200, 20, RED)
            draw_text(f1x1, wWidth-400, 240, 20, ORANGE)
            draw_text(f2x2, wWidth-400, 270, 20, ORANGE)
            draw_text(enc(f1x1)+"*"+enc(const_koef1), wWidth-400, 310, 20, GREEN)
            draw_text(enc(f2x2)+"*"+enc(const_koef2), wWidth-400, 340, 20, GREEN)    
            draw_text(enc(constx1)+"*"+enc(const_koef1), wWidth-500, 370, 20, BROWN)    
            draw_text(enc(constx2)+"*"+enc(const_koef2), wWidth-500, 400, 20, BROWN)    
        except:
            continue
        end_drawing()
    close_window()


from time import time
start_time = time()
main()
print("--- %s seconds ---" % (time() - start_time))