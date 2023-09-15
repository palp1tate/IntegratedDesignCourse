import RPi.GPIO as GPIO
import time

DHTPIN = 17 # GPIO17
MAXTIMINGS = 85

dht11_dat = [0] * 5

def read_dht11_dat():
    laststate = GPIO.HIGH
    counter = 0
    j = 0

    dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0

    GPIO.setup(DHTPIN, GPIO.OUT)
    GPIO.output(DHTPIN, GPIO.LOW)
    time.sleep(0.018)

    GPIO.output(DHTPIN, GPIO.HIGH)
    time.sleep(0.00004)

    GPIO.setup(DHTPIN, GPIO.IN)

    for i in range(MAXTIMINGS):
        counter = 0
        while GPIO.input(DHTPIN) == laststate:
            counter += 1
            time.sleep(0.000001)
            if counter == 255:
                break

        laststate = GPIO.input(DHTPIN)

        if counter == 255:
            break

        if (i >= 4) and (i % 2 == 0):
            dht11_dat[j // 8] <<= 1
            if counter > 16:
                dht11_dat[j // 8] |= 1
            j += 1

    if j >= 40 and dht11_dat[4] == (dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF:
        celsius = dht11_dat[2] + (float)dht11_dat[3] / 10
        fahrenheit = celsius * 1.8 + 32
        humidity = dht11_dat[0] + (float)dht11_dat[1] / 10
        print('Humidity = %.1f %% Temperature = %.1f *C (%.1f *F)' % (humidity, celsius, fahrenheit))


if __name__ == '__main__':
    print('DHT11 Temperature test program')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    while True:
        read_dht11_dat()
        time.sleep(1.0)
