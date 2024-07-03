import pcf8574_io

p1 = pcf8574_io.PCF(0x20)

while True:
    p1.pin_mode("p0", "INPUT")
    print(p1.read("p0"))
