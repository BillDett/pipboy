import os
import time
import pcf8574_io

gpio = pcf8574_io.PCF(0x20)

gpio.pin_mode("p0", "INPUT")
gpio.pin_mode("p1", "INPUT")
gpio.pin_mode("p2", "INPUT")
gpio.pin_mode("p3", "INPUT")
gpio.pin_mode("p4", "INPUT")
gpio.pin_mode("p5", "INPUT")
gpio.pin_mode("p6", "INPUT")
gpio.pin_mode("p7", "INPUT")

while True:
    print("Pin 0: " + str(gpio.read("p0")))
    print("Pin 1: " + str(gpio.read("p1")))
    print("Pin 2: " + str(gpio.read("p2")))
    print("Pin 3: " + str(gpio.read("p3")))
    print("Pin 4: " + str(gpio.read("p4")))
    print("Pin 5: " + str(gpio.read("p5")))
    print("Pin 6: " + str(gpio.read("p6")))
    print("Pin 7: " + str(gpio.read("p7")))
    time.sleep(0.25)
    os.system('clear')
