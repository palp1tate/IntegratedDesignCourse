import time
import wiringpi as wp

makerobo_PCF = 120
makerobo_D0pin = 0
makerobo_Buzz = 1

def makerobo_Print(x):
    if x == 1:
        print("\n*****************")
        print("Makerobo Saft~*")
        print("*****************\n")
    elif x == 0:
        print("\n************************")
        print("* Makerobo Danger Gas! *")
        print("************************\n")
    else:
        print("\n*************************")
        print("* Print value error. *")
        print("*************************\n")

wp.wiringPiSetup() 

if wp.pcf8591Setup(makerobo_PCF, 0x48) == -1:
    print("pcf8591 setup failed")
    exit()

wp.pinMode(makerobo_D0pin, 0)
wp.pinMode(makerobo_Buzz, 1)
wp.digitalWrite(makerobo_Buzz, 1)
makerobo_status = -1
makerobo_count = 0

while True:
    makerobo_analogVal = wp.analogRead(makerobo_PCF + 0)
    print(makerobo_analogVal)

    makerobo_tmp = wp.digitalRead(makerobo_D0pin)

    if makerobo_tmp != makerobo_status:
        makerobo_Print(makerobo_tmp)
        makerobo_status = makerobo_tmp

    if makerobo_status == 0:
        makerobo_count += 1

        if makerobo_count % 2 == 0:
            wp.digitalWrite(makerobo_Buzz, 1)
        else:
            wp.digitalWrite(makerobo_Buzz, 0)
    else:
        makerobo_count = 0
        wp.digitalWrite(makerobo_Buzz, 1)

    time.sleep(0.2)
'''
    需要注意的是，在Python中使用wiringpi需要安装wiringpi-python库。可以通过以下命令安装：
sudo apt-get update
sudo apt-get install wiringpi
sudo pip3 install wiringpi-python
'''
