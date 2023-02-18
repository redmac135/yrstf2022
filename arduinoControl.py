import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

while True:
    time.sleep(2)
    board.digital[9].write(1)
    board.digital[8].write(1)
    print("ON")
    time.sleep(2)
    board.digital[9].write(0)
    board.digital[8].write(0)
    print("OFF")