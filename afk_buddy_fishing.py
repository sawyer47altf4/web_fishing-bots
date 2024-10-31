import pyautogui
import time
import keyboard

def press_and_release(key, duration=0.4):
    """Press and release a key for a specified duration."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def hold_key(key, duration=1):
    """Hold a key down for a specified duration."""
    time.sleep(2) #There is a slow down when you get a fish this corects it.
    with pyautogui.hold(key):
        time.sleep(duration)

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

while True:
    hold_key("a")
    if keyboard.is_pressed("q"):
        break
    
    press_and_release("e")
    if keyboard.is_pressed("q"):
        break
    
    press_and_release("e")
    time.sleep(1)
    press_and_release("c")
    
    hold_key("d")
    if keyboard.is_pressed("q"):
        break
    
    press_and_release("e")
    if keyboard.is_pressed("q"):
        break
    
    press_and_release("e")
    time.sleep(1)
    press_and_release("c")
    
    if keyboard.is_pressed("q"):
        break
