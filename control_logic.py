from globals import TARGET_TEMP_F, HYSTERESIS_C
from RPi import GPIO

def control_fan_heater(temp_c, fan, HEATER_PIN):
    # convert F setpoint to Celsius
    target_c = (TARGET_TEMP_F - 32) * 5/9

    # too cold → turn heater ON
    if temp_c < target_c - HYSTERESIS_C:
        GPIO.output(HEATER_PIN, GPIO.HIGH)
        fan.off()
        return "OFF", "ON"   # Fan, Heater

    # too hot → turn fan ON
    if temp_c > target_c + HYSTERESIS_C:
        fan.on()
        GPIO.output(HEATER_PIN, GPIO.LOW)
        return "ON", "OFF"

    # in the safe band → all OFF
    fan.off()
    GPIO.output(HEATER_PIN, GPIO.LOW)
    return "OFF", "OFF"
