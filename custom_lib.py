import pyautogui
import time
import keyboard

def hold_key(key, duration=1):
    """Hold a key down for a specified duration."""
    with pyautogui.hold(key):
        time.sleep(duration)
        
def press_and_release(key, duration=0.4):
    """Press and release a key for a specified duration."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def mouse_click(duration=0.04, LOR="left"): # LOR = left or right mouse botten
    pyautogui.mouseDown(button=LOR)
    time.sleep(duration)
    pyautogui.mouseUp()
    