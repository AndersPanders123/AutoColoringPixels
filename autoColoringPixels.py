import mouse
import keyboard
from threading import Thread
from os import _exit
from pynput.keyboard import Key, KeyCode, Listener

original_position = None
spawn = mouse.get_position()

def move_mouse():
    global original_position
    duration_moveLeft = 0.4 #Change this value to adjust the speed of the mouse
    duration_moveRight = 0.4 #Change this value to adjust the speed of the mouse back to the original position
    duration_moveDown = 0.01 #Change this value to adjust the speed of the mouse when moving down
    duration_moveUpp = 0.01 #Change this value to adjust the speed of the mouse when moving up

    pixels_down = 4 #Change this value to adjust the amount of pixels the mouse moves down

    while True:
        original_position = mouse.get_position()
        if original_position[1] >= 1000:
            break
        for i in range(5):
            mouse.hold(button='left')
            mouse.move(original_position[0] - 2000, original_position[1], duration=duration_moveLeft)
            mouse.move(*original_position, duration=duration_moveRight)
        mouse.move(original_position[0], original_position[1] + pixels_down, duration_moveDown)

    mouse.move(original_position[0], 0, duration=duration_moveUpp)
    move_mouse()

def reset_mouse():
    if keyboard.is_pressed('r'):
        mouse.move(*original_position)


def main():
    def add_hotkey():
        keyboard.add_hotkey('|', move_mouse)
        keyboard.wait()

    def keyboard_listener():
        def on_press(key: Key):
            if key == Key.esc: _exit(0)
        with Listener(on_press=on_press) as listener:
            listener.join()

    threads = [
        Thread(target=add_hotkey),
        Thread(target=keyboard_listener)
    ]
    for i in threads: i.start()
    for i in threads: i.join()

if __name__ == "__main__":
    main()