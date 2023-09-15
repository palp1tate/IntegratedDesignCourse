import wiringpi as wp
import time

servo_pin = 1

def main():
    print("Servo Test Program")
    
    # 初始化 wiringPi
    wp.wiringPiSetup()
    
    # 设置引脚为 PWM 输出模式
    wp.pinMode(servo_pin, wp.GPIO.PWM_OUTPUT)
    
    # 设置 PWM 模式为 Mark: Space
    wp.pwmSetMode(wp.GPIO.PWM_MODE_MS)
    
    # 设置 PWM 时钟频率和分辨率
    wp.pwmSetClock(192)
    wp.pwmSetRange(2000)
    
    # 控制舵机角度
    print("Current angle: 0")
    wp.pwmWrite(servo_pin, 100)
    time.sleep(1)
    
    print("Current angle: 45")
    wp.pwmWrite(servo_pin, 150)
    time.sleep(1)
    
    print("Current angle: 90")
    wp.pwmWrite(servo_pin, 200)
    time.sleep(1)
    
    print("Current angle: 135")
    wp.pwmWrite(servo_pin, 250)
    time.sleep(1)
    
    print("Current angle: 180")
    wp.pwmWrite(servo_pin, 300)
    time.sleep(1)
    
    # 逐渐改变脉冲宽度，让舵机匀速旋转
    for i in range(761):
        wp.pwmWrite(servo_pin, i)
        time.sleep(0.2)
    
    print("Done")

if __name__ == '__main__':
    main()
