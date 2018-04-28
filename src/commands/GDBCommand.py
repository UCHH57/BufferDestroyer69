#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class GDBCommand(Command):
    command = "gdb"
    help = "\tRun gdb."

    def set_option(self, option, cmd):
        args = ""
        for arg in cmd:
            if arg != "gdb":
                args = args + " " + arg
        system("gdb " + args)
