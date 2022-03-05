#!/bin/bash

#apt update
#apt install python3 python3-pip python3-hidapi libhidapi-hidraw0

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

modprobe dwc2
modprobe -r g_multi
modprobe libcomposite

cd /sys/kernel/config/usb_gadget/
mkdir -p hid_controller
cd hid_controller

echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Joystick Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409 # Localisation
echo "0123456789" > strings/0x409/serialnumber
echo "Raspberry Pi" > strings/0x409/manufacturer
echo "Raspberry Pi Virtual Keyboard" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 200 > configs/c.1/MaxPower
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo "05010906A101050719E029E71500250175019508810295017508810395057501050819012905910295017503910395067508150025650507190029658100C0" | xxd -r -ps > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
ls /sys/class/udc > UDC

echo "[INFO]: A reboot may be required for some changes to take effect"

exit 0
