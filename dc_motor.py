class  DCMotor():


    @classmethod
    def set_motor_effort(cls, effort:float):

        # effort correlates to speed as a function
        # of percent of total voltage supplied (0-1)

        if effort>=0 and effort<=1:
            cls.motor_effort = abs(effort)



    @classmethod
    def set_motor_direction(cls, direction=True):

        # motor direction is defined as a boolean
        # where True is forward and False is backward

        if direction:
            cls.motor_direction = 1
        else:
            cls.motor_direction = -1



    def __init__(self, motor_obj):
        self.motor_obj = motor_obj

        self.set_motor_effort(effort=0)
        self.set_motor_direction(direction=True)



    def drive_motor(self):

        throttle = self.motor_direction * self.motor_effort
        self.motor_obj.throttle=throttle
