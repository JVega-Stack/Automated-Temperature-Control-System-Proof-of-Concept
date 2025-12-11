import time
from dht_sensor import read_temperature_c
from buttons import update_buttons
from control_logic import control_fan_heater
from lcd_display import lcd, update_lcd
from globals import TARGET_TEMP_F
from RPi import GPIO
from gpiozero import OutputDevice

# Hardware pins
HEATER_PIN = 17
FAN_PIN = 18

# Setup fan and heater
GPIO.setup(HEATER_PIN, GPIO.OUT)
GPIO.output(HEATER_PIN, GPIO.LOW)

fan = OutputDevice(FAN_PIN, active_high=False)

def shutdown_system():
    fan.off()
    GPIO.output(HEATER_PIN, GPIO.LOW)
    lcd.clear()
    lcd.write_string("Shutdown...")
    time.sleep(1)
    lcd.clear()
    GPIO.cleanup()

if __name__ == "__main__":
    lcd.write_string("System Booting...")
    time.sleep(2)

    try:
        while True:
            temp_c = read_temperature_c()

            if temp_c is None:
                lcd.clear()
                lcd.write_string("Sensor Error")
                time.sleep(1)
                continue

            temp_f = temp_c * 9/5 + 32

            update_buttons()  # updates TARGET_TEMP_F

            fan_state, heater_state = control_fan_heater(temp_c, fan, HEATER_PIN)

            update_lcd(temp_f, fan_state, heater_state)

            print(f"{temp_f:.1f}F Set:{TARGET_TEMP_F:.1f}F "
                  f"Fan:{fan_state} Heater:{heater_state}")

            time.sleep(1)

    except KeyboardInterrupt:
        shutdown_system()
