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
    time.sleep(2) #There is a slow down when you get a fish this corects it so you dont get off set..
    with pyautogui.hold(key):
        time.sleep(duration)

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

while keyboard.is_pressed("q") == False:
    
    hold_key("a") # move left
    
    press_and_release("e") #check for fish

    press_and_release("e") # if it has a fish this gets you off the "you chought a fish screen"
    time.sleep(1)
    press_and_release("c") # open the emote wheel to fix a bug when you chatch a fish so you can move
      # the rest is the same but in reveres 
    hold_key("d")
    
    press_and_release("e")
    
    press_and_release("e")
    time.sleep(1)
    press_and_release("c")