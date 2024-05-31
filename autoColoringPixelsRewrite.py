from threading import Thread
from os import _exit
from pynput.keyboard import Key, KeyCode, Listener

def move_mouse():
    global original_position
    move_tick_delay = .01
    x = 0
    while True:
        original_position = mouse.position
        if original_position[1] >= 1000:
            print(original_position[0])
            break
        if x >= 1500: break
        mouse.press(Button.left)
        mouse.move(10, 0)
        x += 10
        print()
        time.sleep(move_tick_delay)

    mouse.position = (spawn[0], mouse.position[1] + 15)
    move_mouse()










