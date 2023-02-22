import time

from morse import reference as morse
from braille import reference as braille

from cameraInterface import start_capture as cameraInput
from speechtotext import mp3_to_text
from arduinoControl import output_binary as send_binary

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz1234567890 "
BINARY_PIN = 6
BINARY_TIME_FACTOR = 0.1
AUDIO_FILE_PATH = "test.m4a"
# 1 = audio
# 2 = video
CONFIG = 1 

def clean_string(input_string: str) -> str:
    lowered = input_string.lower()
    split_string = [*lowered]
    for pk, char in enumerate(split_string):
        if char not in ALLOWED_CHARS:
            split_string.pop(pk)
    print(split_string)
    return "".join(split_string)

def output_binary(text: str) -> None:
    cleanned = clean_string(text)
    for char in cleanned:
        if char == " ":
            time.sleep(7*BINARY_TIME_FACTOR)
            print(" ", end="")
        else:
            send_binary(BINARY_TIME_FACTOR, BINARY_PIN, morse[char])
            time.sleep(3*BINARY_TIME_FACTOR)

if __name__ == "__main__":
    if CONFIG == 2:
        text = cameraInput()
        print(text)
        output_binary(text)
    if CONFIG == 1:
        text = mp3_to_text(AUDIO_FILE_PATH)
        print(text)
        output_binary(text)