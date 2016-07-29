from gpiozero import LED
import time

red = LED(18)
amber = LED(23)
green = LED(24)

red.on()
amber.on()
green.on()

time.sleep(0.5)

red.off()
amber.off()
green.off()
