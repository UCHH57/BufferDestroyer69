#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class DisassFunctionsCommand(Command):
    command = "d"
    usage = "[function name]"
    help = "\tDisass a function."

    def set_option(self, option, cmd):
        system("objdump -d " + option.binPath + " | sed '/<" + cmd[1] + ">:/,/^$/!d'")
