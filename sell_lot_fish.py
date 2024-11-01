import pyautogui as ag
import time
import keyboard
# add ETA, for time it will take and add a way to calculate the amount of fish there are
def sell_fish(time_delay, fish_sold):
    ag.click()
    fish_sold += 1
    time.sleep(time_delay)
    return fish_sold

if __name__ == "__main__":
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

    while keyboard.is_pressed("esc") == False:
       print(sell_fish(3, 0))