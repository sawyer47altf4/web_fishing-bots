import pyautogui as ag
import time
import keyboard

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
fish_sold = 0
while True:
    ag.click()
    fish_sold += 1
    print(f"fish sold {fish_sold}")
    time.sleep(3)