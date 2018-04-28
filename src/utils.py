#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Option import BinType


def format_hex_value(hexv, option):

    if hexv.startswith("0x"):
        hexv = hexv[2:]

    if option.binType == BinType.THIRTY_TWO:
        size = 8
    else:
        size = 16

    if len(hexv) > size:
        hexv = hexv[-(size - 2):]
    elif len(hexv) < size:
        hexv = '0' * (size - len(hexv)) + hexv

    tmp = hexv
    hexv = ""

    i = len(tmp) - 1
    while i > 0:
        hexv += "\\x"
        hexv += tmp[i - 1]
        hexv += tmp[i]
        i -= 2

    return hexv
