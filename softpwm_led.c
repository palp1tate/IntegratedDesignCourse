#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>

const int LED = 1;

int main() {
    int level;
    wiringPiSetup(); // 初始化wiringPi
    pinMode(LED, OUTPUT); // 设置引脚输出方向
    softPwmCreate(LED, 1, 100); // 初始化软件PWM，其中1~100是周期范围
    while (1) {
        for (level = 0; level < 101; level++) {
            softPwmWrite(LED, level); // 改变PWM的周期
            delay(10);
        }
        delay(1);
        for (level = 100; level >= 0; level--) {
            softPwmWrite(LED, level);
            delay(10);
        }
        delay(1);
    }
}
