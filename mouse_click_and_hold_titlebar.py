import pyautogui
import time
start = pyautogui.position()
pyautogui.moveTo(Windows (X Position) + (Windows (Width)-15),Windows (Y Position)+7)
old = pyautogui.position()
#pyautogui.drag(30, 0, 10, button='left')

while pyautogui.position() == old:
	pyautogui.mouseDown(button='left')

pyautogui.mouseUp(button='left')
pyautogui.moveTo(start)
quit()

# this is a comment : - )