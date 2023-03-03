from math import sin,cos
from sympy import Symbol, diff, expand
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
    
    const_koef1 = f1#eval(f1.replace("x2",enc(x2_)).replace("x1",enc(x1_)))
    const_koef2 = f2#eval(f2.replace("x2",enc(x2_)).replace("x1",enc(x1_)))   
    print(const_koef1,const_koef2)
    
    f1x1 = enc(const_koef)+"*"+enc(df1x1)
    f1x2 = enc(const_koef)+"*"+enc(df1x2)
    f2x1 = enc(const_koef)+"*"+enc(df2x1)
    f2x2 = enc(const_koef)+"*"+enc(df2x2)
    print(f1x1," ; ",f1x2," ; ",f2x1," ; ",f2x2)
    
    constx1 = str(expand( enc(f1x1) +"+"+enc(f1x2) ))
    constx2 = str(expand( enc(f2x1) +"+"+enc(f2x2) ))
    print(constx1,"        ",constx2)

#==================================================================================================================
    shagt = 0.01
      
    draw4 = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,shagt,wWidth)
    draw4a = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,-shagt,wWidth)
    
    x1_ = x1_*(-1)
    x2_ = x2_*(-1)

    draw8 = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,shagt,wWidth)   
    draw8a = euler(enc(f1x1)+"*"+enc(const_koef1),enc(f2x2)+"*"+enc(const_koef2),x1_,x2_,2000,-shagt,wWidth)  
            
    draw4 = alignwithcenter(draw4,xStart,yStart,mashtab)
    draw4a = alignwithcenter(draw4a,xStart,yStart,mashtab)
    draw8 = alignwithcenter(draw8,xStart,yStart,mashtab)
    draw8a = alignwithcenter(draw8a,xStart,yStart,mashtab)
    
    init_window(wWidth, wHeight, "Hello")
    rl.SetTargetFPS(60)
    while not window_should_close():
        begin_drawing()

        clear_background(WHITE)
        raylib.rlSetLineWidth(3)
        
        raylib.DrawLine(0,yStart,wWidth,yStart,BLACK);
        raylib.DrawLine(xStart,0,xStart,wHeight,BLACK);
        raylib.DrawLine(0,yStart+mashtab,wWidth,yStart+mashtab,LIGHTGRAY);
        raylib.DrawLine(0,yStart-mashtab,wWidth,yStart-mashtab,LIGHTGRAY);
        raylib.DrawLine(xStart+mashtab,0,xStart+mashtab,wHeight,LIGHTGRAY);
        raylib.DrawLine(xStart-mashtab,0,xStart-mashtab,wHeight,LIGHTGRAY);
        
        raylib.DrawLineStrip(draw4, len(draw4), GREEN)
        raylib.DrawLineStrip(draw4a, len(draw4a), GREEN)
        raylib.DrawLineStrip(draw8, len(draw8), (0, 225, 0, 255))
        raylib.DrawLineStrip(draw8a, len(draw8a), (0, 225, 0, 255))
         
        draw_text(in1, wWidth-400, 20, 20, PINK)
        draw_text(in2, wWidth-400, 50, 20, PINK)        
        draw_text(str(X0)+" "+str(tuple([-x for x in X0])), wWidth-400, 80, 20, PINK)        
        draw_text(enc(f1x1)+"*"+enc(const_koef1), wWidth-400, 310, 20, GREEN)
        draw_text(enc(f2x2)+"*"+enc(const_koef2), wWidth-400, 340, 20, GREEN) 
        
        end_drawing()
    close_window()


from time import time
start_time = time()
main()
print("--- %s seconds ---" % (time() - start_time))