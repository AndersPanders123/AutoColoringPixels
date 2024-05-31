from threading import Thread
from os import _exit
from pynput.keyboard import Key, KeyCode, Listener
from pynput.mouse import Button, Controller
import time

mouse = Controller()

original_position = None
spawn = mouse.position

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

def main():

    def on_press(key: Key | KeyCode):
        if key == Key.esc: _exit(0)
        elif key == KeyCode.from_char("r"): mouse.position = spawn
        elif key == KeyCode.from_char("|"): Thread(target=move_mouse).start()
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()