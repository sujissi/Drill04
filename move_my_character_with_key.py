from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('cat_sheet.png')

running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
frame = 0
dir_x, dir_y = 0, 0
dir_img = 0

hide_cursor()
def handle_events():
    global running, dir_x, dir_y, dir_img, frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                dir_img = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                dir_img = 2
            elif event.key == SDLK_UP:
                dir_y += 1
                dir_img = 0
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                dir_img = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
    if dir_x == 0 and dir_y == 0 :
        frame, dir_img = 1, 3

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 52+7, dir_img * 72+9, 35, 35, x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)

close_canvas()