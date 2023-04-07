#include <wiringPi.h>
#include <stdio.h>
#include <sys/time.h>

#define makerobo_Trig 1 //超声波模块Tring控制管脚
#define makerobo_Echo 0 //超声波模块Echo控制管脚

//超声波模块初始化工作
void makerobo_ultraInit(void) {
    pinMode(makerobo_Echo, INPUT); //Echo设置为输入模式
    pinMode(makerobo_Trig, OUTPUT); //Trig设置为输出模式
}

//超声波计算距离函数
float ur_disMeasure(void) {
    struct timeval ur_tv1;
    //定义时间结构体变量ur_tv1
    struct timeval ur_tv2;
    //定义时间结构体变量ur_tv2
    long ur_time1, ur_time2;
    //定义两个长整型时间变量ur_time1,ur_time2
    float ur_dis;
    //定义距离变量

    digitalWrite(makerobo_Trig, LOW); //开始起始
    delayMicroseconds(2); //延时2us

    digitalWrite(makerobo_Trig, HIGH); //超声波启动信号，延时10us
    delayMicroseconds(10); //发出超声波脉冲

    digitalWrite(makerobo_Trig, LOW); //设置为低电平

    while (digitalRead(makerobo_Echo) == 0); //等待回传信号
    gettimeofday(&ur_tv1, NULL); //获取当前时间

    while (digitalRead(makerobo_Echo) == 1); //回传信号截止信息
    gettimeofday(&ur_tv2, NULL); //获取当前时间

    ur_time1 = ur_tv1.tv_sec * 1000000 + ur_tv1.tv_usec; //转换微秒级的时间
    ur_time2 = ur_tv2.tv_sec * 1000000 + ur_tv2.tv_usec; //转换为微秒级时间

    //声速在空气中的传播速度为340m/s，超声波要经历一个发送信号和一个回波信息，
    //计算公式如下所示:
    ur_dis = (float)(ur_time2 - ur_time1) / 1000000 * 34000 / 2; //求出距离

    return ur_dis; //返回距离值
}

//主程序
int main(void) {
    float ur_dis; //定义一个局部变量，保存距离值

    //初始化连接失败时，将消息打印到屏幕
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed!\n");
        return 1;
    }

    makerobo_ultraInit(); //调用超声波模块初始化工作

    //无限循环
    while (1) {
        ur_dis = ur_disMeasure(); //获取超声波计算距离
        printf("%0.2f cm\n", ur_dis); //打印超声波距离值
        delay(300); //延时
    }
    return 0;
}
