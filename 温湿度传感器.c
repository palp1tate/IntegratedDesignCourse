#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MAXTIMINGS 85
#define makerobo_DHTPIN 0

int makerobo_dht11_dat[5] = {0, 0, 0, 0, 0};

void makerobo_read_dht11_dat() {
    uint8_t dht_laststate = HIGH;
    uint8_t makerobo_counter = 0;
    uint8_t j = 0, i;
    float f;

    makerobo_dht11_dat[0] = makerobo_dht11_dat[1] = makerobo_dht11_dat[2] = makerobo_dht11_dat[3] = makerobo_dht11_dat[4] = 0;

    pinMode(makerobo_DHTPIN, OUTPUT);
    digitalWrite(makerobo_DHTPIN, LOW);
    delay(18);

    digitalWrite(makerobo_DHTPIN, HIGH);
    delayMicroseconds(40);

    pinMode(makerobo_DHTPIN, INPUT);

    for (i = 0; i < MAXTIMINGS; i++) {
        makerobo_counter = 0;

        while (digitalRead(makerobo_DHTPIN) == dht_laststate) {
            makerobo_counter++;
            delayMicroseconds(1);

            if (makerobo_counter == 255) {
                break;
            }
        }

        dht_laststate = digitalRead(makerobo_DHTPIN);

        if (makerobo_counter == 255) {
            break;
        }

        if ((i >= 4) && (i % 2 == 0)) {
            makerobo_dht11_dat[j / 8] <<= 1;
            if (makerobo_counter > 16) {
                makerobo_dht11_dat[j / 8] |= 1;
            }
            j++;
        }
    }

    if (j >= 40 &&
        (makerobo_dht11_dat[4] == ((makerobo_dht11_dat[0] + makerobo_dht11_dat[1] + makerobo_dht11_dat[2] + makerobo_dht11_dat[3]) & 0xFF ))) {
        f = makerobo_dht11_dat[2] * 9.0 / 5.0 + 32.0;
        printf("Humidity = %d.%d %% Temperature = %d.%d *C (%.1f *F)\n",
                makerobo_dht11_dat[0], makerobo_dht11_dat[1], makerobo_dht11_dat[2], makerobo_dht11_dat[3], f);
    }
}

int main(void) {
    printf("Makerobo Raspberry Pi wiringPi DHT11 Temperature test program\n");

    if (wiringPiSetup() == -1) {
        exit(1);
    }

    while (1) {
        makerobo_read_dht11_dat();
        delay(1);
    }

    return 0;
}
