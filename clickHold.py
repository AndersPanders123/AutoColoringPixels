from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
import sys  # Import sys module to use sys.exit()

# Global flag to control the holding state
holding = False

def HoldButton():
    global holding
    mouse = MouseController()
    holding = True
    while holding:
        mouse.press(Button.left)
        mouse.release(Button.left)
    print("Stopped holding the button")

def on_press(key):
    global holding
    if key == KeyCode(char='y'):  # Start holding the button when 'y' is pressed
        if not holding:
            HoldButton()
    elif key == KeyCode(char='n'):  # Stop holding the button when 'n' is pressed
        holding = False
    elif key == KeyCode.from_char('\x1b'):  # Check if the Esc key is pressed
        sys.exit()  # Exit the program

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()