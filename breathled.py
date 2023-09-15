import wiringpi
import time

LED = 1

wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(LED, 0, 100)

while True:
    for level in range(0, 101):
        wiringpi.softPwmWrite(LED, level)
        time.sleep(0.01)
    time.sleep(0.001)
    for level in range(100, -1, -1):
        wiringpi.softPwmWrite(LED, level)
        time.sleep(0.01)
    time.sleep(0.001)
