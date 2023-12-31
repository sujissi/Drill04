from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('cat_sheet.png')

running = True
collision = False
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
frame = 0
dir_x, dir_y = 0, 0
dir_img = 0

hide_cursor()
def handle_events():
    global running, dir_x, dir_y, dir_img
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x, dir_img = 1, 1
            elif event.key == SDLK_LEFT:
                dir_x, dir_img = -1, 2
            elif event.key == SDLK_UP:
                dir_y, dir_img = 1, 0
            elif event.key == SDLK_DOWN:
                dir_y, dir_img = -1, 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                dir_y = 0
    if dir_x == 0 and dir_y == 0:
        dir_img = 3

def is_collision(x, y):
    if x < 40 or x > TUK_WIDTH - 40 or y < 40 or y > TUK_HEIGHT - 40:
        return True


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 52+7, dir_img * 72+9, 35, 35, x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    x += dir_x * 10
    y += dir_y * 10
    if is_collision(x, y):
        x -= dir_x * 10
        y -= dir_y * 10
    delay(0.05)

close_canvas()