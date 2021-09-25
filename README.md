# rpigpad
Raspberry Pi Gamepad - Linux Service connecting 2x USB HID Mice into 1x XAC Virtual Joystick for Windows

Ever wanted to use 2 Mice instead of the usual Keyboard and Mouse to play PC games? \
Well now you can! All that's required is a correctly configured Raspberry Pi 4. \
(other models of Pi may work with some tweaking and are as yet untested.)

The service works by using the libcomposite version of the legacy g_hid gadget driver at `/dev/hidg0`. \
This then sends messages across a USB-C to USB-A cable connected to your PC \
with the Pi's on-board DWC2 Controller.

To Install, use `git clone` to create a local copy of the repository (or download as .zip) \
and use `make install`. Feel free to customise the Makefile and Service to find what works.

You will need to edit the `rpigpad.py` file to configure which 2 mice you would like to use. \
It will try to use any HID device it can find, so if you get stuck there's more info there.

If you are unfamiliar with setting up USB Gadgets, you will need to make one edit to `/boot/config.txt` \
and that is to add `dtoverlay=dwc2,dr_mode=peripheral`. Other values for `dr_mode` include `host` and `otg`.
More information: https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget

![screenshot](https://github.com/TheMindVirus/rpigpad/blob/main/screenshot.png)
