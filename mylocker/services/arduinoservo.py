from kink import inject
from time import sleep
from pyfirmata import Arduino, SERVO


@inject
class ArduinoServo:
    def __init__(self):
        self.port = "COM3"
        self.board = Arduino(self.port)

    def rotate_locker_to_90(self, pin):
        self.board.digital[pin + 1].mode = SERVO
        for i in range(90, 0, -1):
            self.board.digital[pin + 1].write(i)
            sleep(0.015)

    def rotate_locker_to_0(self, pin):
        self.board.digital[pin + 1].mode = SERVO
        for i in range(0, 90):
            self.board.digital[pin + 1].write(i)
            sleep(0.015)

    # def rotate_locker_to_90(self, pin):
    #     self.board.digital[pin].mode = SERVO
    #     for i in range(90, 0, -1):
    #         self.board.digital[pin].write(i)
    #         sleep(0.015)
    #
    # def rotate_locker_to_0(self, pin):
    #     self.board.digital[pin].mode = SERVO
    #     for i in range(0, 90):
    #         self.board.digital[pin].write(i)
    #         sleep(0.015)


# rotate_locker_to_90(5)