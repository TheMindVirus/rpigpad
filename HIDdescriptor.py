#https://www.usb.org/sites/default/files/hut1_22.pdf

HIDdescriptor = \
[
    0x05, 0x01, # USAGE_PAGE: Generic
    0x09, 0x04, # USAGE: Joystick
    0xA1, 0x01, # COLLECTION: Application

        0x05, 0x09, # USAGE_PAGE: Button
        0x19, 0x01, # USAGE_MINIMUM: Button 1
        0x29, 0x10, # USAGE_MAXIMUM: Button 16
        0x15, 0x00, # LOGICAL_MINIMUM: 0
        0x25, 0x01, # LOGICAL_MAXIMUM: 1
        0x75, 0x01, # REPORT_SIZE: 1 bit
        0x95, 0x10, # REPORT_COUNT: x16
        0x81, 0x02, # INPUT: Data, Var, Abs
    
        0xA1, 0x00, # COLLECTION: Physical
            0x05, 0x01, # USAGE_PAGE: Generic
            0x09, 0x30, # USAGE: X
            0x09, 0x31, # USAGE: Y
            0x15, 0x00, # LOGICAL_MINIMUM: 0
            0x25, 0xFF, # LOGICAL_MAXIMUM: 255
            0x75, 0x08, # REPORT_SIZE: 8 bits
            0x95, 0x02, # REPORT_COUNT: x2
            0x81, 0x02, # INPUT: Data, Var, Abs
        0xC0, # END_COLLECTION

        0xA1, 0x00, # COLLECTION: Physical
            0x05, 0x01, # USAGE_PAGE: Generic
            0x09, 0x33, # USAGE: Rx
            0x09, 0x34, # USAGE: Ry
            0x15, 0x00, # LOGICAL_MINIMUM: 0
            0x25, 0xFF, # LOGICAL_MAXIMUM: 255
            0x75, 0x08, # REPORT_SIZE: 8 bits
            0x95, 0x02, # REPORT_COUNT: x2
            0x81, 0x02, # INPUT: Data, Var, Abs
        0xC0, # END_COLLECTION
    
    0xC0, # END_COLLECTION
]

HIDformat = \
[
    "Byte0: Buttons 8 -> 1",
    "Byte1: Buttons 16 -> 9",
    "Byte2: Pointer1 X",
    "Byte3: Pointer1 Y",
    "Byte4: Pointer2 X",
    "Byte5: Pointer2 Y",
]

print("[Descriptor]")
data = ""
for byte in HIDdescriptor:
    data += "{:02X}".format(byte)
print(data)
print()

print("[Format]")
data = ""
for line in HIDformat:
    data += line + "\n"
print(data)
print("Length:", str(len(HIDformat)), "bytes")

data = ""

"""
[Descriptor]
05010904A10105091901291015002501750195108102A100050109300931150025FF750895028102C0A100050109330934150025FF750895028102C0C0

[Format]
Byte0: Buttons 8 -> 1
Byte1: Buttons 16 -> 9
Byte2: Pointer1 X
Byte3: Pointer1 Y
Byte4: Pointer2 X
Byte5: Pointer2 Y

Length: 6 bytes
>>> 
"""
