#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

const int LED = 1;

int main(void) {
    int level;
    if (wiringPiSetup() == -1) {
        printf("Error initializing wiringPi\n");
        exit(1);
    }
    pinMode(LED, PWM_OUTPUT);
    for (;;) {
        for (level = 1023; level >= 0; --level) {
            pwmWrite(LED, level);
            delay(1);
        }
        delay(1);
        for (level = 0; level < 1024; ++level) {
            pwmWrite(LED, level);
            delay(1);
        }
        delay(1);
    }
}
