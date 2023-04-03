import smbus
import time

# 对应比较旧的版本如RPI V1版本，则“bus = smbus.SMBus(0)"。当前的版本为V1.1，因此使用1。
bus = smbus.SMBus(1)

# 通过sudo i2cdetect -y -1 可以获取到IIC的地址
def setup(Addr):
    global address
    address = Addr

# 读取模拟量信息
def read(chn):
    try:
        if chn == 0:
            bus.write_byte(address, 0x40)
        elif chn == 1:
            bus.write_byte(address, 0x41)
        elif chn == 2:
            bus.write_byte(address, 0x42)
        elif chn == 3:
            bus.write_byte(address, 0x43)
        bus.read_byte(address)  # 开始进行读取转换
    except Exception as e:
        print("Address: %s" % address)
        print(e)
    return bus.read_byte(address)

# 模块输出模拟量控制，范围为0-255
def write(val):
    try:
        temp = val  # 将数值赋给temp变量
        temp = int(temp)  # 将字符串转换为整型
        # 在终端上打印temp以查看，否则将注释掉
        # print(temp)
        bus.write_byte_data(address, 0x40, temp)
    except Exception as e:
        print("Error: Device address: 0x%2X" % address)
        print(e)

if __name__ == "__main__":
    setup(0x48)
    while True:
        print("AIND =", read(0))
        print("AIN1_=", read(1))
        tmp = read(0)
        # 将0-255转换为125-255，低于125时LED不会亮
        tmp = tmp * (255 - 125) / 255 + 125
        write(tmp)
        time.sleep(0.3)
