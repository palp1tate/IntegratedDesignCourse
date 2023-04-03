#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>
#include <math.h>

#define makerobo_PCF1201 //基础管脚120
#define makerobo_Dopin0l //光敏传感器管脚1

int main() {
    int makerobo_analogVal;
    
    // 初始化wiringPi连接，如果连接失败则打印消息到屏幕并退出程序
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed!\n");
        return 1;
    }
    
    // 在基本引脚120上设置pcf8591，地址0×48
    pcf8591Setup(makerobo_PCF, 0x48);
    
    while (1) { // 无限循环
        // 获取AIN0上的值，读取光敏传感器值
        makerobo_analogVal = analogRead(makerobo_PCF + 0);
        
        // 打印出光敏传感器的值
        printf("Photoresistor Value: %d\n", makerobo_analogVal);
        
        // 延时200ms
        delay(200);
    }
    
    return 0;
}
