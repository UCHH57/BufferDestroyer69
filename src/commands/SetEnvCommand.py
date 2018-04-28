#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class SetEnvCommand(Command):
    command = "se"
    usage = "[variable name] [variable value | \"[shellcode]\"]"
    help = "\tSet an environment variable.\n\tex:\tse TEST /bin/sh or se TEST [shellcode]"

    def set_option(self, option, cmd):

        if cmd[2] == "[shellcode]":
            option.env[cmd[1]] = option.shellcode
        else:
            option.env[cmd[1]] = cmd[2]
