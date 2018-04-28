#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class ChangeShellcodeCommand(Command):
    command = "cshc"
    usage = "[new shellcode]"
    help = "\tChange the schellcode."

    def set_option(self, option, cmd):
        option.shellcode = cmd[1]
