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

#def alignwithcenterdot(dot,xStart,yStart,mashtab):
#    dot[0] = int(xStart + dot[0]*mashtab)
#    dot[1] = int(yStart - dot[1]*mashtab)
#    return dot

def main():
    
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
    kolvotochek = 6
    radiustochek = 1.5
    kolvoshagov = 2000
    shagt = 0.01
    sdvig = 0.2
    
    wWidth = 1400
    wHeight = 1000
    mashtab = 150
    xStart = int(wWidth/2)
    yStart = int(wHeight/2)
    
    drawx1 = enc(f1x1)+"*"+enc(const_koef1)
    drawx2 = enc(f2x2)+"*"+enc(const_koef2)
    drawp = False
    drawp1= False
    
    if in1[:3]=="x2=":
        #pinkdraw = euler(enc(shagt),in1[4:],0,0,int(kolvoshagov/2),shagt,wWidth)
        x1 = [elem/10 for elem in range (-100,100)]
        pinkdraw = [[]]
        for iii,elem in enumerate(x1):
            pinkdraw.append([x1[iii],eval(in1[3:].replace("^","**").replace("x1",enc(x1[iii])))])
        pinkdraw = pinkdraw[1:]
        pinkdraw = alignwithcenter(pinkdraw,xStart,yStart,mashtab)
        drawp = True
    if in2[:3]=="x1=":
        x2 = [elem/10 for elem in range (-100,100)]
        pinkdraw1 = [[]]
        for iii,elem in enumerate(x2):
            pinkdraw1.append([eval(in2[3:].replace("^","**").replace("x2",enc(x2[iii]))),x2[iii],])
        pinkdraw1 = pinkdraw1[1:]
        pinkdraw1 = alignwithcenter(pinkdraw1,xStart,yStart,mashtab)
        drawp1 = True
    
    tocki = [[]]
    for ii in range(kolvotochek):
        xtemper = eval(enc(radiustochek)+"*"+"cos"+enc(ii+sdvig))
        ytemper = eval(enc(radiustochek)+"*"+"sin"+enc(ii+sdvig))
        temper = []
        temper.append(xtemper)
        temper.append(ytemper)
        tocki.append(temper)
    tocki = tocki[1:]
    
    big_draw_f = [[]]
    big_draw_f_o = [[]]
    for ii in range(kolvotochek):
        draw_f = euler(drawx1,drawx2,tocki[ii][0],tocki[ii][1],kolvoshagov,shagt,wWidth)
        draw_f_obr = euler(drawx1,drawx2,tocki[ii][0],tocki[ii][1],kolvoshagov,-shagt,wWidth)        
        draw_f = alignwithcenter(draw_f,xStart,yStart,mashtab)
        draw_f_obr = alignwithcenter(draw_f_obr,xStart,yStart,mashtab)
        big_draw_f.append(draw_f)
        big_draw_f_o.append(draw_f_obr)
    big_draw_f = big_draw_f[1:]
    big_draw_f_o = big_draw_f_o[1:]
    
    
    
    init_window(wWidth, wHeight, "mpp")
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
        raylib.DrawCircle(xStart,yStart,5,BLACK)
        raylib.DrawCircleLines(xStart,yStart,radiustochek*mashtab,LIGHTGRAY)


        for ii in range(kolvotochek):        
            raylib.DrawLineStrip(big_draw_f[ii], len(big_draw_f[ii]), (0,abs(255-20*ii),48,255))
            raylib.DrawLineStrip(big_draw_f_o[ii], len(big_draw_f_o[ii]), (0,abs(255-20*ii),48,255))
        
        if drawp:
            raylib.DrawLineStrip(pinkdraw, len(pinkdraw),PINK)
        if drawp1:
            raylib.DrawLineStrip(pinkdraw1, len(pinkdraw1),PINK)
                 
        draw_text(in1, wWidth-400, 20, 20, PINK)
        draw_text(in2, wWidth-400, 50, 20, PINK)        
        draw_text(drawx1, wWidth-500, 80, 20, GREEN)
        draw_text(drawx2, wWidth-500, 110, 20, GREEN)
        for ii,elem in enumerate(tocki):
            draw_text(enc(elem), wWidth-500, 140+30*ii, 20, GRAY)

        for ii in range(kolvotochek):
            raylib.DrawCircle(int(xStart + tocki[ii][0]*mashtab),int(yStart - tocki[ii][1]*mashtab),5,DARKGREEN)
 
        end_drawing()
    close_window()


from time import time
start_time = time()
main()
print("--- %s seconds ---" % (time() - start_time))

"""
def euler1tocka(func,x,itercount,shag):
    znachenia = []
    y = eval(func.replace("x1",enc(x)).replace("x2",enc(x)))
    for _ in range(itercount):
        y = y + shag * eval(func.replace("x1",enc(x)).replace("x2",enc(x)))
        x+=shag
        znachenia.append(y)
    znachenia = znachenia[1:]
    return znachenia
"""