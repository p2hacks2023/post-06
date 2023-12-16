import serial
import struct
import time
import array

# Constants
FRAME_HEADER = 0x55
CMD_SERVO_MOVE = 0x03
CMD_ACTION_GROUP_RUN = 0x06
CMD_ACTION_GROUP_STOP = 0x07
CMD_ACTION_GROUP_SPEED = 0x0B
CMD_GET_BATTERY_VOLTAGE = 0x0F

BATTERY_VOLTAGE = 0x0F
ACTION_GROUP_RUNNING = 0x06
ACTION_GROUP_STOPPED = 0x07
ACTION_GROUP_COMPLETE = 0x08

def get_low_byte(val):
    return val & 0xFF

def get_high_byte(val):
    return (val >> 8) & 0xFF

def byte_to_hw(a, b):
    return (a << 8) | b

class LobotServoController:
    def __init__(self, port_name):
        self.serial = serial.Serial(port_name, 9600, timeout=1) # 9600 is bps
        self.num_of_action_group_running = 0xFF
        self.action_group_run_times = 0
        self.is_get_battery_volt = False
        self.is_running_ = False
        self.battery_voltage = 0

    # 個別のサーボを動かしたいときの関数
    def move_servo(self, servo_id, position, time_):
        if servo_id > 31 or time_ <= 0:
            return

        buf = array.array('B', [
            FRAME_HEADER, FRAME_HEADER, 8, CMD_SERVO_MOVE, 1,
            get_low_byte(time_), get_high_byte(time_), servo_id,
            get_low_byte(position), get_high_byte(position)
        ])

        self.serial.write(buf)
        
    # まとめてサーボを動かしたいときの関数
    def moveServos(self, servos, Time):
        Num = len(servos)
        buf = bytearray()
        if Num < 1 or Num > 32 or not Time > 0:
            return
        buf.append(FRAME_HEADER)
        buf.append(FRAME_HEADER)
        buf.append(Num * 3 + 5)
        buf.append(CMD_SERVO_MOVE)
        buf.append(Num)
        buf.append(get_low_byte(Time))
        buf.append(get_high_byte(Time))
        for servo in servos:
            buf.append(servo["ID"])
            buf.append(get_low_byte(servo["Position"]))
            buf.append(get_high_byte(servo["Position"]))
        self.serial.write(buf)