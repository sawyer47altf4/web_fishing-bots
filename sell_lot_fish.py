import pyautogui
import time
import keyboard
# add ETA, for time it will take and add a way to calculate the amount of fish there are
# want to add counter out put to file so i can plot my fish i catch 

"""sells fish then add it to a counter called fish sold"""
def sell_fish(time_delay, fish_sold):
    while keyboard.is_pressed("esc") == False:
        pyautogui.click()
        fish_sold += 1
        time.sleep(time_delay)
        print(fish_sold)
    with open("output.csv", "a") as output:
        output.write(str(fish_sold) + "\n")

if __name__ == "__main__":
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

    sell_fish(3, 0)