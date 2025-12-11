import time
from RPi import GPIO
from globals import TARGET_TEMP_F

BTN_UP = 22
BTN_DOWN = 27

GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def update_buttons():
    global TARGET_TEMP_F

    if GPIO.input(BTN_UP):
        TARGET_TEMP_F += 1
        time.sleep(0.2)

    if GPIO.input(BTN_DOWN):
        TARGET_TEMP_F -= 1
        time.sleep(0.2)
