import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

class ArduinoControl:
    def __init__(self, morse_pin: int, braille_start_pin: int, time_factor: float) -> None:
        self.time_factor = time_factor
        self.morse_pin = morse_pin
        self.braille_start_pin = braille_start_pin
        board.digital[morse_pin].write(1)
        print("Initalized Board")
    
    def output_braille(self, code: list) -> None:
        for pk, value in enumerate(code, self.braille_start_pin):
            if value == 1:
                board.digital[pk].write(0) 
            if value == 0:
                board.digital[pk].write(1)

    def output_morse(self, code: list) -> None:
        for char in code:
            if char == 1:
                print(".", end="")
                board.digital[self.morse_pin].write(0)
                time.sleep(self.time_factor)
                board.digital[self.morse_pin].write(1)
            if char == 2:
                print("_", end="")
                board.digital[self.morse_pin].write(0)
                time.sleep(3*self.time_factor)
                board.digital[self.morse_pin].write(1)
            time.sleep(self.time_factor)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        board.digital[6].write(1)
        print("ON")
        time.sleep(0.1)
        board.digital[6].write(0)
        print("OFF")