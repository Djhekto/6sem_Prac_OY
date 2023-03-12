from pyray import *
import raylib#<--- pylance podcvechivaet lisheee bez etogo

def calc_nocenter_rectangle(up_left,down_right,mashtab):
    down_right[0]=int((down_right[0]-up_left[0])*mashtab)
    down_right[1]=int((down_right[1]-up_left[1])*mashtab)
    return up_left,down_right

def drawgridinrectangle(up_left,down_right_wh,mashtab,razmer,tolshina):
    otctup = razmer*mashtab
    iteracii = int(down_right_wh[1]/otctup)
    for i in range(iteracii+1):
        v1 = Vector2(up_left[0],up_left[1]+i*otctup)
        v2 = Vector2(down_right_wh[0]+up_left[0],up_left[1]+i*otctup) 
        raylib.DrawLineEx(v1,v2,tolshina,LIGHTGRAY)
    iteracii = int(down_right_wh[0]/otctup)
    for i in range(iteracii+1):
        v1 = Vector2(up_left[0]+i*otctup,up_left[1])
        v2 = Vector2(up_left[0]+i*otctup,down_right_wh[1]+up_left[1]) 
        raylib.DrawLineEx(v1,v2,tolshina,LIGHTGRAY)
    
    return

def main():
    wWidth = 1280
    wHeight = 960
    mashtab = 2
    razmer = 20
    up_left = [300,300]
    down_right = [600,500]
    up_left,down_right_wh = calc_nocenter_rectangle(up_left,down_right,mashtab)
    
    init_window(wWidth, wHeight, "kvadratic na chernom")
    raylib.SetTargetFPS(60)
    while not window_should_close():
        begin_drawing()

        clear_background(BLACK)
        raylib.rlSetLineWidth(3)
        
        rec1 = Rectangle(100,100,80,80)
        raylib.DrawRectangleGradientEx(rec1,RED,ORANGE,PINK,BLUE)
        
        rec3 = Rectangle(up_left[0],int(up_left[1]+down_right_wh[1]/2),int(down_right_wh[0]/2),int(down_right_wh[1]/2))  
        raylib.DrawRectangleGradientEx(rec3,(230, 41, 55, 255),(255,161, 0, 255),(255, 109, 194, 255),(0, 121, 241,255))  
        rec3copy = Rectangle(up_left[0]+2,int(up_left[1]+down_right_wh[1]/2)+4,int(down_right_wh[0]/2)-6,int(down_right_wh[1]/2)-4) 
        raylib.DrawRectangleGradientEx(rec3copy,BLACK,BLACK,BLACK,BLACK)          
        raylib.DrawRectangleGradientEx(rec3copy,(230, 41, 55, 100),(255,161, 0, 100),(255, 109, 194, 100),(0, 121, 241,100))

        rec2 = Rectangle(up_left[0],up_left[1],down_right_wh[0],down_right_wh[1])        
        raylib.DrawRectangleLinesEx(rec2,2,RAYWHITE)
        drawgridinrectangle(up_left,down_right_wh,mashtab,razmer,1)
        
        end_drawing()
    close_window()

main()