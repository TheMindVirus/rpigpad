#!/bin/bash

apt update
apt install python3 python3-pip python3-hidapi libhidapi-hidraw0

modprobe dwc2
modprobe -r g_multi
modprobe libcomposite

cd /sys/kernel/config/usb_gadget/
mkdir -p xac_joystick
cd xac_joystick

echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Joystick Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
echo 0xEF > bDeviceClass
echo 0x02 > bDeviceSubClass
echo 0x01 > bDeviceProtocol

mkdir -p strings/0x409 # Localisation
echo "0123456789" > strings/0x409/serialnumber
echo "Raspberry Pi" > strings/0x409/manufacturer
echo "Raspberry Pi Virtual Gamepad" > strings/0x409/product

mkdir -p functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 3 > functions/hid.usb0/report_length

#Report Descriptor #Utter Nonsense
#echo "05010904A1011581257F0901A10009300931750895028102C005091901290815002501750195088102C0" | xxd -r -ps > functions/hid.usb0/report_desc
echo "05010904A10105091901291015002501750195108102A100050109300931150025FF750895028102C0A100050109330934150025FF750895028102C0C0" | xxd -r -ps > functions/hid.usb0/report_desc

mkdir -p configs/c.1
mkdir -p configs/c.1/strings/0x409
echo 0x80 > configs/c.1/bmAttributes
echo 200 > configs/c.1/MaxPower # 200mA
echo "XAC configuration" > configs/c.1/strings/0x409/configuration
ln -s functions/hid.usb0 configs/c.1
ls /sys/class/udc > UDC

chmod -R 775 /sys/kernel/config/usb_gadget/xac_joystick

echo "[INFO]: A reboot may be required for some changes to take effect"

exit 0
