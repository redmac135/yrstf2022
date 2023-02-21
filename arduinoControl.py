import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

def output_braille(code: list) -> None:
    for pk, value in enumerate(code, 8): # start at pin 8
        board.digital[pk].write(value) 

while True:
    time.sleep(2)
    board.digital[8].write(1)
    print("ON")
    time.sleep(2)
    board.digital[8].write(0)
    print("OFF")