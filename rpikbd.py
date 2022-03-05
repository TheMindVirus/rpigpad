#!/usr/bin/python3
# Raspberry Pi Virtual Keyboard Service (rpigpad.py) - Alastair Cota 05/03/2022 @ 07:51
#
# Currently set up to act as a HID Keyboard for controlling console games
# with keyboard support on the USB-OTG port of the Raspberry Pi Zero W
# with the aim of turning it into a Parsec Node
#
# sudo pip3 install hidapi
# sudo apt-get install libhidapi-hidraw0
# Install and Run "Raspberry Pi Virtual Keyboard" with GNU Make:
#     make install | make play | make remove
#
# If at all you lose control of your virtual keyboard or any connected device,
# Please disconnect and reconnect them while this service is not running
# and control will return back to the Console. (Ctrl+C to exit)
#

import os, sys, time, atexit

DEVICE = "/dev/hidg0"
kbd = None

KEY_RELEASE = (chr(0) * 8)

KEY_W = (chr(0) * 2 + chr(26) + chr(0) * 5)
KEY_S = (chr(0) * 2 + chr(22) + chr(0) * 5)
KEY_A = (chr(0) * 2 + chr(4) + chr(0) * 5)
KEY_D = (chr(0) * 2 + chr(7) + chr(0) * 5)

KEY_CTRL = (chr(1) + chr(0) * 7)
KEY_SHIFT = (chr(2) + chr(0) * 7)
KEY_ALT = (chr(3) + chr(0) * 7)

KEY_SPACE = (chr(0) * 2 + chr(44) + chr(0) * 5)
KEY_ENTER = (chr(0) * 2 + chr(40) + chr(0) * 5)
KEY_ESC = (chr(0) * 2 + chr(41) + chr(0) * 5)

def report(action):
    global kbd
    kbd = open(DEVICE, "wb")
    kbd.write(action.encode())
    kbd.close()

def setup():
    global kbd
    cleanup()

def loop():
    global kbd
    while True:
        try:
            print("CTRL")
            report(KEY_CTRL)
            time.sleep(0.25)
            report(KEY_RELEASE)
            time.sleep(0.25)
        except Exception as error:
            #raise error
            print(error, file = sys.stderr)
            time.sleep(1)
            setup()

def cleanup():
    report(KEY_RELEASE)
    time.sleep(0.1)

if __name__ == "__main__":
    atexit.register(cleanup)
    setup()
    loop()
