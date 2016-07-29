import os
import time
from gpiozero import LED, Button, Buzzer

red = LED(18)
amber = LED(23)
green = LED(24)
buzzer = Buzzer(22)
button = Button(25)

# Define a function for the initial state - Green LED on, rest off
# If you have the second 'pedestrian LEDs', turn the red on & green off
def StartGreen():
	# all code is indented
	print("Starting green")

# Turn the green off and the amber on for 3 seconds
# Pedestrian red LED stays lit
def SteadyAmber():
	# all code is indented
	print("Steady amber")

# Turn the amber off, and then the red on for 1 second
def SteadyRed():
	# all code is indented
	print("Steady red")

# Sound the buzzer for 4 seconds
# If you have the pedestrian LEDs, turn the red off and green on
def StartWalking():
	# Make the buzzer buzz on and off, half a second of
	# sound followed by half a second of silence
	print("Start walking")

# Turn the buzzer off and wait for 2 seconds
# If you have the pedestrian LEDs, make the green one flash on
# and off for two seconds
def DontWalk():
	# all code is indented
	print("Don't walk!")

# Flash the amber on and off for 6 seconds
# and the green pedestrian LED too
def FlashingAmberGreen():
	# all code is indented
	print("Flashing amber and pedestrian green")

# Flash the amber for one more second
# Turn the green pedestrian LED off and the red on
def FlashingAmber():
	# all code is indented
	print("Flashing amber")

# Go through the traffic light sequence by calling each function
# one after the other
def TrafficLightSequence():
	# all code is indented
	print("Traffic light sequence")

os.system("clear")
print("Traffic Lights")

# Initialise the traffic lights
StartGreen()

# Here is the loop that waits at least 20 seconds before stopping the
# cars if the button has been pressed

while True: # Loop forever
	start = time.time()
	while button.is_pressed == False:
		time.sleep(0.1)
		if button.is_pressed:
			print("Button has been pressed")
			now = time.time()
			if (now-start) <= 20:
				print("Waiting for 20-(now-start)")
				time.sleep(20 - (now-start))
			TrafficLightSequence()

