import time
import wiringpi

makerobo_PCF = 120 # 基础管脚120
makerobo_Dopin0l = 1 # 光敏传感器管脚1

# 初始化wiringPi连接，如果连接失败则打印消息到屏幕并退出程序
wiringpi.wiringPiSetup()

# 在基本引脚120上设置pcf8591，地址0×48
wiringpi.pcf8591Setup(makerobo_PCF, 0x48)

while True: # 无限循环
    # 获取AIN0上的值，读取光敏传感器值
    makerobo_analogVal = wiringpi.analogRead(makerobo_PCF + 0)

    # 打印出光敏传感器的值
    print("Photoresistor Value: {}".format(makerobo_analogVal))

    # 延时200ms
    time.sleep(0.2)
