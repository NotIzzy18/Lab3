from machine import Pin
from time import sleep

led = Pin(18, Pin.OUT) # declare pins
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
led.off() # initial state is off

recentlydepressed=False
while True:
    if sw5.value()==1:
        recentlydepressed=True # waiting...
    if sw5.value()==0 and recentlydepressed:
        led.value(led.value()^1) # toggle by flipping the bit
        sleep(0.02) # delay to avoid button bouncing
    recentlydepressed=False