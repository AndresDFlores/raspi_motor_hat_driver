import time
import board
from adafruit_motorkit import MotorKit
from dc_motor import *


kit = MotorKit(i2c=board.I2C())

motor1 = DCMotor(motor_obj=kit.motor1)
motor2 = DCMotor(motor_obj=kit.motor2)
motor3 = DCMotor(motor_obj=kit.motor3)
motor4 = DCMotor(motor_obj=kit.motor4)


motor1.set_motor_effort(effort=0.25)
motor1.set_motor_direction(direction=True)
motor1.drive_motor()

motor2.set_motor_effort(effort=0.25)
motor2.set_motor_direction(direction=False)
motor2.drive_motor()

motor3.set_motor_effort(effort=0)
motor3.drive_motor()

motor4.set_motor_effort(effort=0)
motor4.drive_motor()


time.sleep(3)


motor1.set_motor_effort(effort=0.25)
motor1.set_motor_direction(direction=False)
motor1.drive_motor()

motor2.set_motor_effort(effort=0)
motor2.set_motor_direction(direction=True)
motor2.drive_motor()

motor3.set_motor_effort(effort=0)
motor3.drive_motor()

motor4.set_motor_effort(effort=0)
motor4.drive_motor()


time.sleep(3)


motor1.set_motor_effort(effort=0)
motor1.set_motor_direction(direction=True)
motor1.drive_motor()
