
import uvage

screen_height = 600
screen_width = 800
camera = uvage.Camera(screen_width, screen_height)
b1 = uvage.from_color(50, 50, "red", 40, 40)
b2 = uvage.from_color(0, 0, "white", 1, 600)
b3 = uvage.from_color(400, -10, "white", 800, 0)
b5 = uvage.from_color(400, 600, "white", 800, 0)
f1 = uvage.from_color(300, 600, "black", 600, 20)
f21 = uvage.from_color(50, 480, "black", 600, 20)
f22 = uvage.from_color(850, 480, "black", 600, 20)
f31 = uvage.from_color(250, 360, "black", 600, 20)
f32 = uvage.from_color(1050, 360, "black", 600, 20)
f41 = uvage.from_color(50, 240, "black", 600, 20)
f42 = uvage.from_color(850, 240, "black", 600, 20)
f5 = uvage.from_color(500, 120, "black", 600, 20)
is_moving = False

def floors():
    if not b1.touches(b3):
        if f1.touches(b3):
            f1.y += 620
        else:
            f1.y -= 3
        if f21.touches(b3):
            f21.y += 620
        else:
            f21.y -= 3
        if f22.touches(b3):
            f22.y += 620
        else:
            f22.y -= 3
        if f31.touches(b3):
            f31.y += 620
        else:
            f31.y -= 3
        if f32.touches(b3):
            f32.y += 620
        else:
            f32.y -= 3
        if f41.touches(b3):
            f41.y += 620
        else:
            f41.y -= 3
        if f42.touches(b3):
            f42.y += 620
        else:
            f42.y -= 3
        if f5.touches(b3):
            f5.y += 620
        else:
            f5.y -= 3

    camera.draw(f1)
    camera.draw(f21)
    camera.draw(f22)
    camera.draw(f31)
    camera.draw(f32)
    camera.draw(f41)
    camera.draw(f42)
    camera.draw(f5)
def move_rectangle():
    global is_moving
    if uvage.is_pressing('left arrow'):
        if b1.x == 20:
            is_walking = False
        else:
            b1.x -= 10
            is_walking = True
    elif uvage.is_pressing('right arrow'):
        if b1.x == 780:
            is_walking = False
        else:
            b1.x += 10
            is_walking = True
    if b1.touches(b3):
        if uvage.is_pressing('left arrow') or uvage.is_pressing('right arrow'):
            b1.x = 0
        is_walking = False

    b1.yspeed += 3
    if (f1.touches(b1) or f21.touches(b1) or f22.touches(b1) or f31.touches(b1)
            or f32.touches(b1) or f41.touches(b1)
            or f42.touches(b1) or f5.touches(b1) or b1.touches(b5)):
        b1.move_to_stop_overlapping(f1)
        b1.move_to_stop_overlapping(f21)
        b1.move_to_stop_overlapping(f22)
        b1.move_to_stop_overlapping(f31)
        b1.move_to_stop_overlapping(f32)
        b1.move_to_stop_overlapping(f41)
        b1.move_to_stop_overlapping(f42)
        b1.move_to_stop_overlapping(f5)
        b1.move_to_stop_overlapping(b5)
        b1.yspeed = 0
    b1.move_speed()

    camera.draw(b1)

def gameover():
    if b1.touches(b3):
        camera.draw("GAME OVER", 100, "red", 400, 300)
        camera.draw("GAME OVER", 100, "red", 400, 300)
        camera.draw("GAME OVER", 100, "red", 400, 300)
def tick():
    camera.clear('white')
    floors()
    move_rectangle()
    gameover()
    camera.display()


uvage.timer_loop(60, tick)
