import mouse
import keyboard
from threading import Thread
from os import _exit
from pynput.keyboard import Key, Listener

def move_mouse():
    duration_moveLeft = 0.35 #Change this value to adjust the speed of the mouse
    duration_moveRight = 0.35 #Change this value to adjust the speed of the mouse back to the original position
    duration_moveDown = 0.01 #Change this value to adjust the speed of the mouse when moving down
    duration_moveUpp = 0.01 #Change this value to adjust the speed of the mouse when moving up
    while True:
        original_position = mouse.get_position()
        if original_position[1] >= 1000:
            print(original_position[0])
            break
        mouse.hold(button='left')
        mouse.move(original_position[0] - 2000, original_position[1], duration=duration_moveLeft)
        mouse.move(*original_position, duration=duration_moveRight)
        mouse.move(original_position[0], original_position[1] + 2, duration_moveDown)

    mouse.move(original_position[0], 0, duration=duration_moveUpp)
    move_mouse()

def main():
    def add_hotkey():
        keyboard.add_hotkey('|', move_mouse)
        keyboard.wait()
    def safe_exit():
        def on_press(key: Key):
            if key == Key.esc: _exit(0)
        with Listener(on_press=on_press) as listener:
            listener.join()
    threads = [
        Thread(target=add_hotkey),
        Thread(target=safe_exit)
    ]
    for i in threads: i.start()
    for i in threads: i.join()

if __name__ == "__main__":
    main()