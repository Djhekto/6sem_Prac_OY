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

    str_font = load_font("resources/fonts/romulus.png");
    gui_set_font(str_font)
    
    str_fun1 = " "
    str_log1 = False
    str_vec1 = down_right[0]+10,up_left[1]+30
    str_rec1 = Rectangle(down_right[0]+10,up_left[1]+10,200,40)
    
    init_window(wWidth, wHeight, "kvadratic na chernom")
    raylib.SetTargetFPS(10)
    while not window_should_close():
        begin_drawing()

        clear_background(WHITE)
        raylib.rlSetLineWidth(3)
        
        raylib.DrawRectangleV(up_left,down_right,(240, 245, 245, 255))
        drawgridinrectangle(up_left,down_right,grid_center_x, grid_center_y,mashtab_grid,razmer,1)
        raylib.DrawCircle(grid_center_x, grid_center_y, 2, BLACK); 
        
        raylib.DrawRectangle(down_right[0], 0, wWidth, wHeight, (255,250,250,255))
        raylib.DrawRectangle(0, down_right[1], wWidth, wHeight, (255,250,250,255))

#derived from raylib/examples/text_input_box.c
        raylib.DrawRectangleLinesEx(str_rec1,3,GRAY)
        if (raylib.CheckCollisionPointRec(raylib.GetMousePosition(), str_rec1)): str_log1 = True;
        else: str_log1 = False
        if str_log1:
            raylib.SetMouseCursor(raylib.MOUSE_CURSOR_IBEAM);
            key = raylib.GetCharPressed();
            while (key > 0):
                if key >= 32 and key <= 125:
                    str_fun1 = str_fun1+chr(key)
                key = raylib.GetCharPressed();
        if raylib.IsKeyPressed(raylib.KEY_BACKSPACE):
            str_fun1 = str_fun1[:-1]
        else:
            raylib.SetMouseCursor(raylib.MOUSE_CURSOR_DEFAULT);
#потом raylib/examples/text_rectangle_bounds.c
        #raylib.DrawText(str_fun1,str_rec1[0],str_rec1[1],3,BLACK)
        draw_text_ex(str_font,str_fun1,str_vec1,20,1,BLACK)
        
        end_drawing()
    close_window()

main()