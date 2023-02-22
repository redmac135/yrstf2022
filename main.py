import time

from morse import reference as morse
from braille import reference as braille

from cameraInterface import start_capture as cameraInput
from speechtotext import mp3_to_text
from arduinoControl import ArduinoControl

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz1234567890 "
MORSE_PIN = 6
BRAILLE_START_PIN = 8
MORSE_TIME_FACTOR = 0.1
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
    return "".join(split_string)

def parse_morse(control: ArduinoControl, text: str) -> None:
    for char in text:
        if char == " ":
            time.sleep(7*MORSE_TIME_FACTOR)
            print(" ", end="")
        else:
            control.output_morse(morse[char])
            time.sleep(3*MORSE_TIME_FACTOR)

if __name__ == "__main__":
    control = ArduinoControl(MORSE_PIN, BRAILLE_START_PIN, MORSE_TIME_FACTOR)
    if CONFIG == 2:
        text = cameraInput()
    if CONFIG == 1:
        text = mp3_to_text(AUDIO_FILE_PATH)
    cleanned = clean_string(text)
    print("Raw Captured Text: " + text)
    print("Cleanned Text: " + cleanned)
    parse_morse(control, cleanned)