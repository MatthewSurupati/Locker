from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM3'
pin = 4
board = Arduino(port)

board.digital[pin].mode = SERVO

def rotateServo(pin, angel):
    board.digital[pin].write(angel)
    sleep(0.015)

while True:
    for i in range(0, 180):
        # print(f'i = {i}')
        rotateServo(pin, i)

    for i in range(180, 1, -1):
        rotateServo(pin, i)