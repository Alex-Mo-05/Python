from pynput.mouse import Button, Controller
import time


mouse = Controller()


count = int(input("Number of clicks: "))
interval = int(input("Interval (Seconds): "))

time.sleep(5)



for i in range(count):
    mouse.click(Button.left, 2)
    time.sleep(interval)
