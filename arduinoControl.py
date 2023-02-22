import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

def output_braille(code: list) -> None:
    for pk, value in enumerate(code, 8): # start at pin 8
        board.digital[pk].write(value) 

def output_binary(time_factor: int, pin: int, code: list) -> None:
    for char in code:
        if char == 1:
            print(".", end="")
            board.digital[pin].write(1)
            time.sleep(time_factor)
            board.digital[pin].write(0)
        if char == 2:
            print("_", end="")
            board.digital[pin].write(1)
            time.sleep(3*time_factor)
            board.digital[pin].write(0)
        time.sleep(time_factor)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        board.digital[6].write(1)
        print("ON")
        time.sleep(0.1)
        board.digital[6].write(0)
        print("OFF")