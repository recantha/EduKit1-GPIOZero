import os
import time
from gpiozero import LED

red = LED(18)
amber = LED(23)
green = LED(24)

os.system("clear")
print("Which LED would you like to blink?")
print("1: Red")
print("2: Amber")
print("3. Green")

led_choice = input("Choose your LED: ")
count = input("How many times would you like it to blink? ")

led_choice = int(led_choice)
count = int(count)

if led_choice == 1:
	chosen_led = red
elif led_choice == 2:
	chosen_led = amber
elif led_choice == 3:
	chosen_led = green

if led_choice > 0:
	while count > 0:
		chosen_led.on()
		time.sleep(1)
		chosen_led.off()
		time.sleep(1)
		count = count - 1


