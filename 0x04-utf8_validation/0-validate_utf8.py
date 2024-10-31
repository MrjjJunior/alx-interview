#!/usr/bin/python3
""" utf8 validation """


def validUTF8(data):
    """ utf8 validation """
    bytes_remain = 0

    for number in data:
        byte = number & 0xFF

        if bytes_remain == 0:
            if (byte >> 5) == 0b110:
                bytes_remain = 1
            elif (byte >> 4) == 0b1110:
                bytes_remain = 2
            elif (byte >> 3) == 0b11110:
                bytes_remain = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_remain -= 1

    return bytes_remain == 0
