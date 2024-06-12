import os
import math
import time

from threading import Thread

from pynput.keyboard import Key, KeyCode, Listener as KeyboardListener
from pynput.mouse import Button, Controller as MouseController



# Variables

mouse = MouseController()

proportions = [0, 0]

start = None
stop = None

spawn = [0, 0]



# Prompting

while True:
    i = input("Enter artwork proportions (x:y):\n\t")

    if not ":" in i:
        print("Input missing delimiter (:)!")
        continue

    try: proportions[0] = int(i.split(":")[0])
    except:
        print("Given X is not a valid integer!")
        continue

    try: proportions[1] = int(i.split(":")[1])
    except:
        print("Given Y is not a vlid integer!")
        continue

    break



# Keyboard listener

def main():
    global spawn

    if start == None: return print("Start coord not set! Use key \"1\"!")
    if stop == None: return print("Stop coord not set! Use key \"2\"!")

    mouse.press(Button.left)

    while True:

        for y in range(
            start[1], stop[1],
            math.floor(
                (stop[1] - start[1])
                / (proportions[1] - 1)
            )
        ):
            for x in range(
                start[0], stop[0],
                math.floor(
                    (stop[0] - start[0])
                    / (proportions[0] - 1)
                )
            ):
                mouse.position = [x, y]
                time.sleep(.05)

def on_press(key: Key | KeyCode):

    if key == KeyCode.from_char("|"): Thread(target=main).start()

    elif key == KeyCode.from_char("r"): mouse.position = spawn

    elif key == KeyCode.from_char("1"):
        global start
        start = mouse.position
        print("Start coord set!")

    elif key == KeyCode.from_char("2"):
        global stop
        stop = mouse.position
        print("Stop coord set!")

    elif key == Key.esc: os._exit(0)

with KeyboardListener(on_press=on_press) as listener: listener.join()