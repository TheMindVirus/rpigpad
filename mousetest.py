#!/usr/bin/python3
#sudo pip3 install hidapi
#sudo apt-get install libhidapi-hidraw0
#sudo python3 mousetest.py
#(must be run as sudo)
import hid, sys, time, atexit

SELECTED = 0 #e.g. Disabled Second Mouse turned into Left Stick

device = None

def setup():
    global device
    selected = -1
    device = None
    devices = hid.enumerate()
    for i in range(0, len(devices)):
        if (i == SELECTED):
            selected = i
        print("[INFO]: ID:", i, "(Selected)" if (i == selected) else "")
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
    if (selected > -1):
        device = hid.device()
        device.open_path(devices[selected]["path"])
        print(dir(device))

def loop():
    global device
    while True:
        try:
            data = device.read(64)
            print(data)
        except Exception as error:
            #raise error
            print(error, file = sys.stderr)
            time.sleep(1)
            setup()

def cleanup():
    if device:
        device.close()

if __name__ == "__main__":
    atexit.register(cleanup)
    setup()
    loop()
