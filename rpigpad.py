#!/usr/bin/python3
# Raspberry Pi Virtual Gamepad Service (rpigpad.py) - Alastair Cota 25/09/2021 @ 18:45
#
# Currently set up to combine 2x official Raspberry Pi Mice into
# 1x USB HID Compliant Gamepad over the USB-C Connector
# using the DWC2 Controller in USB Gadget Mode
#
# sudo pip3 install hidapi
# sudo apt-get install libhidapi-hidraw0
# Install and Run "Raspberry Pi Virtual Gamepad" with GNU Make:
#     make install | make play | make remove
#
# If at all you lose control of your keyboards, mice or any other HID device,
# Please disconnect and reconnect them while this service is not running
# and control will return back to the Operating System. (Ctrl+C to exit)
#

import hid, os, sys, time, atexit

MOUSE1 = 0 #TODO: Select Actual Mouse 1
MOUSE2 = 1 #TODO: Select Actual Mouse 2
GAMEPAD = "/dev/hidg0"

mouse1 = None
mouse2 = None
gamepad = None

def setup():
    global mouse1, mouse2, gamepad
    mouse1 = None
    mouse2 = None
    selected1 = -1
    selected2 = -1

    print("[INFO]: Reconnecting...")
    devices = hid.enumerate()
    for i in range(0, len(devices)):
        tags = []
        if (i == MOUSE1):
            selected1 = i
            tags.append("Mouse1")
        if (i == MOUSE2):
            selected2 = i
            tags.append("Mouse2")

        print("[INFO]: ID:", i, *tags)
        print("[INFO]: Manufacturer:", devices[i]["manufacturer_string"])
        print("[INFO]: Product:", devices[i]["product_string"])
        print("[INFO]: Path:", devices[i]["path"].decode())
        print("[INFO]: VendorID:", "{:04X}".format(devices[i]["vendor_id"]))
        print("[INFO]: ProductID:", "{:04X}".format(devices[i]["product_id"]))
        print("[INFO]: SerialNo:", devices[i]["serial_number"])
        print("[INFO]: ReleaseNo:", devices[i]["release_number"])
        print("[INFO]: InterfaceNo:", devices[i]["interface_number"])
        print("[INFO]: UsagePage:", devices[i]["usage_page"])
        print("[INFO]: Usage:", devices[i]["usage"])
        print()

    if (selected1 > -1):
        mouse1 = hid.device()
        mouse1.open_path(devices[selected1]["path"])
        mouse1.set_nonblocking(True)
    if (selected2 > -1):
        mouse2 = hid.device()
        mouse2.open_path(devices[selected2]["path"])
        mouse2.set_nonblocking(True)
    gamepad = open(GAMEPAD, "wb")

def loop():
    global mouse1, mouse2, gamepad
    report = [0x00] * 6
    data1 = [0] * 4
    data2 = [0] * 4
    while True:
        try:
            valid = False
            tmp1 = mouse1.read(4)
            tmp2 = mouse2.read(4)
            if (len(tmp1) == 4):
                data1 = tmp1
                valid = True
            if (len(tmp2) == 4):
                data2 = tmp2
                valid = True

            if valid:
                scroll1 = 16 if (data1[3] == 255) else 8 if (data1[3] == 1) else 0
                scroll2 = 16 if (data2[3] == 255) else 8 if (data2[3] == 1) else 0
                if (data1[3] != 0):
                    data1[3] = 0
                if (data2[3] != 0):
                    data2[3] = 0

                report[0] = data1[0] + scroll1
                report[1] = data2[0] + scroll2
                report[2] = data1[1]
                report[3] = data1[2]
                report[4] = data2[1]
                report[5] = data2[2]

                gamepad.write(bytearray(report))
                gamepad.flush()

                #BUG: Scroll Off Messages are not sent by the Mouse
                if (scroll1 != 0) or (scroll2 != 0):
                    report[0] = data1[0]
                    report[1] = data2[0]
                    time.sleep(0.03)
                    gamepad.write(bytearray(report))
                    gamepad.flush()

            #time.sleep(0.001)

        except Exception as error:
            #raise error
            print(error, file = sys.stderr)
            time.sleep(1)
            setup()

def cleanup():
    if mouse1:
        mouse1.close()
    if mouse2:
        mouse2.close()
    if gamepad:
        gamepad.close()

if __name__ == "__main__":
    atexit.register(cleanup)
    setup()
    loop()