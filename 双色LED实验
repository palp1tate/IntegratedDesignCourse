#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define makerobo_Led_PinRed 1    // 定义红色 LED 的引脚为 1
#define makerobo_Led_PinGreen 2  // 定义绿色 LED 的引脚为 2

void makerobo_led_Init(void) {
    softPwmCreate(makerobo_Led_PinRed, 0, 100);
    softPwmCreate(makerobo_Led_PinGreen, 0, 100);
}

void makerobo_led_ColorSet(unsigned char r_val, unsigned char g_val) {
    softPwmWrite(makerobo_Led_PinRed, r_val);
    softPwmWrite(makerobo_Led_PinGreen, g_val);
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed !");
        return 1;
    }
    makerobo_led_Init();
    while (1) {
        makerobo_led_ColorSet(0xff, 0x00);
        delay(500);
        makerobo_led_ColorSet(0x00, 0xff);
        delay(500);
        makerobo_led_ColorSet(0xff, 0x45);
        delay(500);
        makerobo_led_ColorSet(0xff, 0xff);
        delay(500);
        makerobo_led_ColorSet(0x7c, 0xfc);
        delay(500);
    }
    return 0;
}
