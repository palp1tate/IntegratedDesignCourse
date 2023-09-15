#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define uchar unsigned char
#define makerobo_pirPin 0
//PIR人体热释电管脚PIN
#define makerobo_redPin 1
//红色LED灯管脚PIN
#define makerobo_greenPin 2
//绿色LED灯管脚PIN
#define makerobo_bluePin 3
//蓝色LED灯管脚PIN

//RGB-LED 初始化
void makerobo_ledInit(void) {
    softPwmCreate(makerobo_redPin, 0, 100);//初始化PWM
    softPwmCreate(makerobo_greenPin, 0, 100);
    softPwmCreate(makerobo_bluePin, 0, 100);
}

//设置RGB-LED灯颜色
void makerobo_ledColorSet(uchar r_val, uchar g_val, uchar b_val) {
    softPwmWrite(makerobo_redPin, r_val);//设置PWM值
    softPwmWrite(makerobo_greenPin, g_val);
    softPwmWrite(makerobo_bluePin, b_val);
}

int main(void) {
    int makerobo_pir_val;

    //初始化连接失败时，将消息打印到屏幕
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed ! ");
        return 1;
    }

    makerobo_ledInit();
    //初始化LED灯模块
    pinMode(makerobo_pirPin, INPUT);// PIR 模块设置为输入模式

    while (1) {
        makerobo_pir_val = digitalRead(makerobo_pirPin);//检测PIR管脚
        if (makerobo_pir_val == 1) { //如果检测到为高电平
            makerobo_ledColorSet(0xff, 0xff, 0x00);
        }
        else {//如果检测到为低电平
            makerobo_ledColorSet(0x00, 0x00, 0xff);
        }
    }

    return 0;
}
