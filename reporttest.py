#Install and Run "Raspberry Pi Virtual Gamepad" with GNU Make
import os, sys, time

joystick = None

def setup():
    global joystick
    print("[INFO]: Reconnecting...")
    joystick = open("/dev/hidg0", "wb")

def loop():
    global joystick
    while True:
        try:
            print(joystick_report())
            joystick.write(joystick_report())
            joystick.flush()
            time.sleep(0.01)
        except Exception as error:
            print(error, file = sys.stderr)
            setup()
            time.sleep(1)

def joystick_report():
    report = [0] * 6
    report[0] = 0xFF
    report[1] = 0xFF
    report[2] = 0x00
    report[3] = 0xFF
    report[4] = 0x00
    report[5] = 0x00
    return bytearray(report)

if __name__ == "__main__":
    setup()
    loop()