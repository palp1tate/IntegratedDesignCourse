import wiringpi
import time

makerobo_Led_PinRed = 1    # 定义红色 LED 的引脚为 1
makerobo_Led_PinGreen = 2  # 定义绿色 LED 的引脚为 2

def makerobo_led_Init():
    wiringpi.softPwmCreate(makerobo_Led_PinRed, 0, 100)
    wiringpi.softPwmCreate(makerobo_Led_PinGreen, 0, 100)

def makerobo_led_ColorSet(r_val, g_val):
    wiringpi.softPwmWrite(makerobo_Led_PinRed, r_val)
    wiringpi.softPwmWrite(makerobo_Led_PinGreen, g_val)

if wiringpi.wiringPiSetup() == -1:
    print("setup wiringPi failed !")
    exit(1)

makerobo_led_Init()

while True:
    makerobo_led_ColorSet(0xff, 0x00)
    time.sleep(0.5)
    makerobo_led_ColorSet(0x00, 0xff)
    time.sleep(0.5)
    makerobo_led_ColorSet(0xff, 0x45)
    time.sleep(0.5)
    makerobo_led_ColorSet(0xff, 0xff)
    time.sleep(0.5)
    makerobo_led_ColorSet(0x7c, 0xfc)
    time.sleep(0.5)
import wiringpi

makerobo_Led_PinRed = 1
makerobo_Led_PinGreen = 2

def makerobo_led_Init():
    wiringpi.softPwmCreate(makerobo_Led_PinRed, 0, 100)
    wiringpi.softPwmCreate(makerobo_Led_PinGreen, 0, 100)

def makerobo_led_ColorSet(r_val, g_val):
    wiringpi.softPwmWrite(makerobo_Led_PinRed, r_val)
    wiringpi.softPwmWrite(makerobo_Led_PinGreen, g_val)

if __name__ == '__main__':
    if wiringpi.wiringPiSetup() == -1:
        print("setup wiringPi failed !")
        exit(1)
    makerobo_led_Init()
    while True:
        makerobo_led_ColorSet(0xff, 0x00)
        wiringpi.delay(500)
        makerobo_led_ColorSet(0x00, 0xff)
        wiringpi.delay(500)
        makerobo_led_ColorSet(0xff, 0x45)
        wiringpi.delay(500)
        makerobo_led_ColorSet(0xff, 0xff)
        wiringpi.delay(500)
        makerobo_led_ColorSet(0x7c, 0xfc)
        wiringpi.delay(500)
