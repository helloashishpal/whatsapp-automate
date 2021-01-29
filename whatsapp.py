import random
import pyautogui
from time import sleep
while True:
    move_keys = ['right', 'left']
    random_move = random.choice(move_keys)
    pyautogui.press(random_move)
    # sleep(random.randrange(0,4))
    # pyautogui.press('right')
    # pyautogui.press('right')
    # pyautogui.press('left')
    # pyautogui.press('random(pyautogui.LEFT,pyautogui.RIGHT)')

    