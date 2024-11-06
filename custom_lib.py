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
    
def go_to_lake():
    hold_key("a", 3.2)
    hold_key("s", 15)
    press_and_release("1")
    
def get_bait_out():
    press_and_release("b")
    time.sleep(0.5)
    pyautogui.click(x=576, y=485)
    time.sleep(0.5)
    press_and_release("b")
    
def check_bait():
        #x=1856, y=1027 90, 117, 90
    bait_pixel =  pyautogui.pixel(1856, 1027)
    if bait_pixel != (90, 117, 90):
        get_more_bait()
        
def get_more_bait():
    press_and_release("w", 14)
    press_and_release("a", 1)
    press_and_release("e")
    pyautogui.click(x=284, y=373)
    pyautogui.click(x=284, y=373)
    press_and_release("e")
    press_and_release("d", 1)
    press_and_release("s", 14)

def check_for_fish():
    real = pyautogui.pixel(374, 723)
    if real != (156, 145, 74):
        click_fast = True
    else:
        click_fast = False

#def catch_fish():

#def check_for_clicks_on_rod():
    
