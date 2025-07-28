import board
from adafruit_motorkit import MotorKit
from dc_motor import *

import pygame
import sys


class MotorDriver():

	def __init__(self):
		
		
		# Initialize pygame
		self.pg = pygame
		self.pg.init()

		# Set up display (required for handling events in pygame)
		screen = self.pg.display.set_mode((50, 50))
		self.pg.display.set_caption("Key Press Reader")
		
		self.running = True
		
		
		# initialize motors
		kit = MotorKit(i2c=board.I2C())

		self.motor1 = DCMotor(motor_obj=kit.motor1)  # left motor
		self.motor2 = DCMotor(motor_obj=kit.motor2)  # right motor

		self.motor_effort = 0.5
		
		
		
	def drive(self):
		
		for event in self.pg.event.get():

			if event.type == self.pg.KEYDOWN:  # Check for key press
				pressed_key = self.pg.key.name(event.key)  # Output the key pressed
				if pressed_key == 'up':
					print('FORWARD')
					self.motor1.set_motor_effort(effort=self.motor_effort)
					self.motor1.set_motor_direction(direction=True)
					self.motor1.drive_motor()

					self.motor2.set_motor_effort(effort=self.motor_effort)
					self.motor2.set_motor_direction(direction=True)
					self.motor2.drive_motor()
					
					
				elif pressed_key == 'down':
					print('REVERSE')
					self.motor1.set_motor_effort(effort=self.motor_effort)
					self.motor1.set_motor_direction(direction=False)
					self.motor1.drive_motor()

					self.motor2.set_motor_effort(effort=self.motor_effort)
					self.motor2.set_motor_direction(direction=False)
					self.motor2.drive_motor()
					
					
				elif pressed_key == 'left':
					print('LEFT')
					self.motor1.set_motor_effort(effort=self.motor_effort)
					self.motor1.set_motor_direction(direction=False)
					self.motor1.drive_motor()

					self.motor2.set_motor_effort(effort=self.motor_effort)
					self.motor2.set_motor_direction(direction=True)
					self.motor2.drive_motor()
					
					
				elif pressed_key == 'right':
					print('RIGHT')
					self.motor1.set_motor_effort(effort=self.motor_effort)
					self.motor1.set_motor_direction(direction=True)
					self.motor1.drive_motor()

					self.motor2.set_motor_effort(effort=self.motor_effort)
					self.motor2.set_motor_direction(direction=False)
					self.motor2.drive_motor()
					
					
				elif pressed_key == 'space' or pressed_key == 'escape':
					print('SESSION TERMINATED')
					self.running = False
					self.motor1.set_motor_effort(effort=0)
					self.motor1.set_motor_direction(direction=True)
					self.motor1.drive_motor()

					self.motor2.set_motor_effort(effort=0)
					self.motor2.set_motor_direction(direction=True)
					self.motor2.drive_motor()
					
				else:
					print(f'{pressed_key}: NO DEFINED ACTION')
					
					
			elif event.type == self.pg.KEYUP:
				print('NO PRESSED KEY')
				self.motor1.set_motor_effort(effort=0)
				self.motor1.set_motor_direction(direction=True)
				self.motor1.drive_motor()

				self.motor2.set_motor_effort(effort=0)
				self.motor2.set_motor_direction(direction=True)
				self.motor2.drive_motor()
                
				
			if event.type == self.pg.QUIT:  # Exit condition
				print('SESSION TERMINATED')           
				self.running = False
				self.motor1.set_motor_effort(effort=0)
				self.motor1.set_motor_direction(direction=True)
				self.motor1.drive_motor()

				self.motor2.set_motor_effort(effort=0)
				self.motor2.set_motor_direction(direction=True)
				self.motor2.drive_motor()

		
			
	def main(self):
		while self.running:
			self.drive()

	
