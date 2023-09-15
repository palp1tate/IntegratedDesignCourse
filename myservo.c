#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

const int servo_Pin = 1;

int main(void)
{
    printf("Servo Test Program\n");

    if (wiringPiSetup() == -1) {
        printf("Can not initialize wiringPi\n");
        exit(1);
    }

    pinMode(servo_Pin, PWM_OUTPUT);
    pwmSetMode(PWM_MODE_MS);
    pwmSetClock(192);
    pwmSetRange(2000);

    printf("Current angle: 0\n");
    pwmWrite(servo_Pin, 100);

    printf("Current angle: 45\n");
    pwmWrite(servo_Pin, 150);

    printf("Current angle: 90\n");
    pwmWrite(servo_Pin, 200);

    printf("Current angle: 135\n");
    pwmWrite(servo_Pin, 250);

    printf("Current angle: 180\n");
    pwmWrite(servo_Pin, 300);

    for (int i = 0; i <= 760; i++) {
        pwmWrite(servo_Pin, i);
        delay(200);
    }

    printf("Done\n");
    return 0;
}
