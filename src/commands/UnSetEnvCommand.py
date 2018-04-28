#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class UnSetEnvCommand(Command):
    command = "unset"
    usage = "[variable name]"
    help = "\tUnset an environment variable."

    def set_option(self, option, cmd):
        del option.env[cmd[1]]
