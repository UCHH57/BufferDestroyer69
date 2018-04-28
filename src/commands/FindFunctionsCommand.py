#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class FindFunctionsCommand(Command):
    command = "ff"
    usage = "[function name]"
    help = "\tGet a function address.\n\tex:\tff system"

    def set_option(self, option, cmd):
        system('(echo "b main"; echo "r"; echo "p ' + cmd[1] + '") | gdb ' + option.binPath +
               ' 2>/dev/null | grep "' + cmd[1] + '" | tr " " "\n" | tail -n2 | head -n1')
