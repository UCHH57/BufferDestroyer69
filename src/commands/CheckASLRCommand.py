#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Output import Output


class CheckASLRCommand(Command):
    command = "cASLR"
    output = Output()
    help = "\tCheck if ASLR is On or Off."

    def set_option(self, option, cmd):
        f = open("/proc/sys/kernel/randomize_va_space", "r")
        nb = int(f.read())

        if nb == 2:
            self.output.write_message("ASLR is ON")
        else:
            self.output.write_message("ASLR is OFF")
