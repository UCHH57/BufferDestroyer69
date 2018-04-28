#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class SetVariableValueCommand(Command):
    command = "svv"
    usage = "[value]"
    help = "\tSet a value into a variable.\n\tex:\tsvv 0xdeadbeef or svv 12345"

    def set_option(self, option, cmd):

        if cmd[1].startswith("0x"):
            hnb = cmd[1]
        else:
            hnb = hex(int(cmd[1]))

        if len(hnb) > 10:
            return
        elif len(hnb) < 10:
            tmp = '0' * (10 - len(hnb)) + hnb[2:]
        else:
            tmp = hnb[2:]

        value = ""
        i = len(tmp) - 1
        while i > 0:
            value += "\\x"
            value += tmp[i - 1]
            value += tmp[i]
            i -= 2

        if option.buffSize:
            option.payload = '"\\x90" * ' + str(option.buffSize) + ' + "' + value + '" * 500'
        else:
            option.payload = '"' + value + '" * 500'
