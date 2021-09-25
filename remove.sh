#!/bin/bash

modprobe -rf usb_f_acm
modprobe -rf usb_f_rndis
modprobe -rf usb_f_hid
modprobe -rf libcomposite

rm -rf /sys/kernel/config/usb_gadget/xac_joystick

echo "[INFO]: A reboot may be required for some changes to take effect"

exit 0
