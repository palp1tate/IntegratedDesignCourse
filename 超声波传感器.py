import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

makerobo_Trig = 17  # 超声波模块Tring控制管脚
makerobo_Echo = 27  # 超声波模块Echo控制管脚

# 超声波模块初始化工作
def makerobo_ultraInit():
    GPIO.setup(makerobo_Echo, GPIO.IN)  # Echo设置为输入模式
    GPIO.setup(makerobo_Trig, GPIO.OUT)  # Trig设置为输出模式

# 超声波计算距离函数
def ur_disMeasure():
    GPIO.output(makerobo_Trig, GPIO.LOW)  # 开始起始
    time.sleep(0.000002)  # 延时2us

    GPIO.output(makerobo_Trig, GPIO.HIGH)  # 超声波启动信号，延时10us
    time.sleep(0.00001)  # 发出超声波脉冲

    GPIO.output(makerobo_Trig, GPIO.LOW)  # 设置为低电平

    while GPIO.input(makerobo_Echo) == 0:  # 等待回传信号
        pass
    ur_time1 = time.time()  # 获取当前时间

    while GPIO.input(makerobo_Echo) == 1:  # 回传信号截止信息
        pass
    ur_time2 = time.time()  # 获取当前时间

    # 声速在空气中的传播速度为340m/s，超声波要经历一个发送信号和一个回波信息，
    # 计算公式如下所示:
    ur_dis = (ur_time2 - ur_time1) * 34000 / 2  # 求出距离

    return ur_dis  # 返回距离值

# 主程序
if __name__ == '__main__':
    try:
        makerobo_ultraInit()  # 调用超声波模块初始化工作
        while True:  # 无限循环
            ur_dis = ur_disMeasure()  # 获取超声波计算距离
            print("%0.2f cm" % ur_dis)  # 打印超声波距离值
            time.sleep(0.3)  # 延时
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
