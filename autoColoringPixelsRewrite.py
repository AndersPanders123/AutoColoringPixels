import mouse
import keyboard
from threading import Thread
from os import _exit
from pynput.keyboard import Key, KeyCode, Listener

original_position = None
spawn = mouse.get_position()

def main():
    move_mouse()


def move_mouse():
    global original_position
    duration_moveLeft = 0.1 #Change this value to adjust the speed of the mouse
    duration_moveRight = 0.1 #Change this value to adjust the speed of the mouse back to the original position
    duration_moveDown = 0.01 #Change this value to adjust the speed of the mouse when moving down
    duration_moveUpp = 0.01 #Change this value to adjust the speed of the mouse when moving up
    while True:
        original_position = mouse.get_position()
        if original_position[1] >= 1000:
            break
        mouse.hold(button='left')
        mouse.move(original_position[0] - 1000, original_position[1], duration=duration_moveLeft)
        mouse.move(*original_position, duration=duration_moveRight)
        mouse.move(original_position[0], original_position[1] + 15, duration_moveDown)

    mouse.move(original_position[0], 0, duration=duration_moveUpp)
    move_mouse()

def reset_mouse():
    if keyboard.is_pressed('r'):
        mouse.move(*original_position)

def keyboard_listener():
    def on_press(key: Key | KeyCode):
        if key == Key.esc: _exit(0)
        elif key == KeyCode.from_char("r"): mouse.position = spawn
        elif key == KeyCode.from_char("|"): Thread(target=main).start()
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()