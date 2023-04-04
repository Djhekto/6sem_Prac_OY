from pyray import *
import raylib#<--- pylance podcvechivaet lisheee bez etogo

def grid_mashtab(up_left,down_right,mashtab):
    down_right[0]=int((down_right[0]-up_left[0])*mashtab)
    down_right[1]=int((down_right[1]-up_left[1])*mashtab)
    return up_left,down_right

def grid_center(up_left,down_right):
    return int((up_left[0]+down_right[0])/2), int((up_left[1]+down_right[1])/2)

def drawgridinrectangle(up_left,down_right,grid_center_x, grid_center_y,mashtab,razmer,tolshina):
    otctup = razmer*mashtab
    iteracii = int(down_right[1]/otctup/2)

    for i in range(-iteracii,iteracii+1):
        v1 = Vector2(grid_center_x+i*otctup,up_left[1])
        v2 = Vector2(grid_center_x+i*otctup,down_right[1])
        if i==0:
            raylib.DrawLineEx(v1,v2,tolshina+1,BLACK)
            continue
        raylib.DrawLineEx(v1,v2,tolshina,BLACK)
    
    for i in range(-iteracii,iteracii+1):
        v1 = Vector2(up_left[0],grid_center_y+i*otctup)
        v2 = Vector2(down_right[0],grid_center_y+i*otctup)
        if i==0:
            raylib.DrawLineEx(v1,v2,tolshina+1,BLACK)
            continue        
        raylib.DrawLineEx(v1,v2,tolshina,BLACK)
    return

def main():
    wWidth = 1280
    wHeight = 960
    mashtab_grid = 2.5
    razmer = 20
    up_left = [2,2]
    down_right = [302,302]
    up_left,down_right = grid_mashtab(up_left,down_right,mashtab_grid)
    grid_center_x, grid_center_y = grid_center(up_left,down_right)
    
    init_window(wWidth, wHeight, "kvadratic na chernom")
    raylib.SetTargetFPS(60)
    while not window_should_close():
        begin_drawing()

        clear_background((240,240,255,255))
        raylib.rlSetLineWidth(3)
        
        drawgridinrectangle(up_left,down_right,grid_center_x, grid_center_y,mashtab_grid,razmer,1)
        raylib.DrawCircle(grid_center_x, grid_center_y, 2, BLACK); 
        raylib.DrawRectangle(down_right[0], 0, wWidth, wHeight, (255,250,250,255))
        raylib.DrawRectangle(0, down_right[1], wWidth, wHeight, (255,250,250,255))
        
        
        end_drawing()
    close_window()

main()