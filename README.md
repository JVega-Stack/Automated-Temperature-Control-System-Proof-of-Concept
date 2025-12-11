# Automated-Temperature-Control-System-Proof-of-Concept
A standalone temperature control system built on a Raspberry Pi 3 using a DHT11 sensor, pushbuttons, and an I2C LCD. Automatically activates cooling or heating based on a user-defined setpoint with hysteresis control.

Automated Temperature Control System

Python • Raspberry Pi 3 • DHT11 Sensor • I2C LCD • GPIO Control • systemd

Overview

The Automated Temperature Control System is a standalone thermostat built using a Raspberry Pi 3. It reads real-time temperature data from a DHT11 sensor and automatically activates a cooling fan or a heating element (represented by an LED) based on a user-defined setpoint. The system includes two pushbuttons that allow the user to raise or lower the temperature setpoint, and a 16×2 I2C LCD displays the current temperature, setpoint, and the status of both outputs.

A small hysteresis band prevents rapid switching of the heater and fan. The entire program can run automatically at boot using a custom systemd service, allowing the device to operate as an independent controller.

This project demonstrates Python-based embedded programming, sensor integration, digital I/O control, LCD communication, and deployment of a persistent background service.

Features

Real-time temperature measurement from a DHT11 sensor

Live display of temperature, setpoint, fan state, and heater state

Up/down buttons for temperature adjustment

Automatic cooling and heating control using hysteresis

Clear, organized multi-file Python structure

Fully autonomous operation using systemd

Breadboard prototype wiring suitable for extension

Hardware Used

Raspberry Pi 3 Model B

DHT11 temperature sensor (3-pin)

16×2 I2C LCD with PCF8574 interface

Fan module (active-high control via OutputDevice)

Red LED + 330 Ω resistor for heater indication

Two pushbuttons (Setpoint Up / Setpoint Down)

4.7 kΩ pull-down resistor (if used externally)

Elegoo 5V breadboard power supply module

Prototype board / breadboard

Jumper wires

Wiring Summary
Component	Raspberry Pi Pin	Notes
DHT11 Data	GPIO 4	Uses 5V and GND
Fan (Cooling)	GPIO 18	Active low with OutputDevice
Heater LED	GPIO 17	With current-limiting resistor
Button – Up	GPIO 22	Pull-down
Button – Down	GPIO 27	Pull-down
LCD SDA	GPIO 2	I2C
LCD SCL	GPIO 3	I2C

Module Descriptions
main.py

Controls the main program loop:

Reads temperature

Updates buttons

Executes control logic

Updates LCD

Manages shutdown

dht_sensor.py

Handles communication with the DHT11 sensor and provides temperature in Celsius.

buttons.py

Reads the Up/Down pushbuttons and adjusts the global setpoint.

control_logic.py

Contains the thermostat logic:

Compares measured temperature to setpoint

Applies hysteresis

Turns fan/heater on or off

lcd_display.py

Provides LCD initialization and formatted display functions.

globals.py

Stores shared variables such as:

TARGET_TEMP_F

HYSTERESIS_C

Future Improvements

Add humidity sensing and control

Log data over time to CSV or a database

Add a web dashboard for remote monitoring

Replace prototype wiring with a custom PCB

3D-print a full enclosure for final deployment

Author

Jonathan Vega
Electrical & Computer Engineering Technology
Valencia College – ECET
