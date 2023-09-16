import serial.tools.list_ports
from colorama import init, Fore, Back, Style
import serial
import time
def sxg_arduino_Win32():
    print("v1.000Alfa")
    print("------------------")
    print("  SXSERVISE CLI")
    print("------------------")
    print("Detect Arduino - 0")
    print("LED control    - 1")
    print("Sensor control - 2")
    sxg_arduino_win32_input_command = int(input(Fore.BLUE + ">>> "))
    if sxg_arduino_win32_input_command == 0:
        detect_arduino()
    elif sxg_arduino_win32_input_command == 1:
        arduino = serial.Serial('COM4', 9600)
        def turn_on_led():
            arduino.write(b'1')
        def turn_off_led():
            arduino.write(b'0')
        print("------------------")
        print("  Led control")
        print("------------------")
        print("On - 0")
        print("Off- 1")
        print("exit- 2")
        led_control_command = int(input(Fore.BLUE + ">>> "))
        if led_control_command == 0:
            turn_on_led()
        elif led_control_command == 1:
            turn_off_led()
        elif led_control_command == 2:
            sxg_arduino_Win32()
        else:
            print("Not found.")
            sxg_arduino_win32_input_command()
    elif sxg_arduino_win32_input_command == 2:
        print("------------------")
        print("  Sensor control")
        print("------------------")
        print("Temperature sensor - 0")
        print("exit    - 1")
        sensor_control_input_command = int(input(Fore.BLUE + ">>> "))
        if sensor_control_input_command == 0:
            def read_temperature():
                arduino.write(b't')
                time.sleep(1)
                temperature = arduino.readline().decode().strip()
                return float(temperature)
        elif sensor_control_input_command == 1:
            sxg_arduino_Win32()
        else:
            print("Not Found.")
    else:
        print("Not found.")
        sxg_arduino_Win32()
def detect_arduino():
    print("Finding the arduino may not work. This is a test feature.")
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]    
    if arduino_ports:
        print("Arduino board found on port:", arduino_ports[0])
    else:
        print("Arduino board not found.")
