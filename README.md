# rpikbd
Raspberry Pi Keyboard - Linux Service for emulating a HID Keyboard for Games Consoles

Ever wanted to create your own teabagging machine for Halo: The Master Chief Collection? \
Well now you can! All that's required is a correctly configured Raspberry Pi Zero. \
(other models of Pi may work with some tweaking and are as yet untested.)

![screenshot](https://github.com/TheMindVirus/rpigpad/blob/rpikbd/screenshot.png)

## Installation
The service works by using the libcomposite version of the legacy g_hid gadget driver at `/dev/hidg0`. \
This then sends messages across a microUSB to USB-A cable connected to your Console \
with the Pi's on-board DWC2 Controller.

To Install, use `git clone` to create a local copy of the repository (or download as .zip) \
and use `make install`. Feel free to customise the Makefile and Service to find what works.

You will need to edit the `rpikbd.py` file to add more HID Keycodes that aren't already listed. \
The official Universal Serial Bus Human Interface Device (USB-HID) Specification has more information.

If you are unfamiliar with setting up USB Gadgets, you will need to make one edit to `/boot/config.txt` \
and that is to add `dtoverlay=dwc2,dr_mode=peripheral`. Other values for `dr_mode` include `host` and `otg`. \
More information: https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget
