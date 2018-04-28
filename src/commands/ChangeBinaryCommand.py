#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class ChangeBinaryCommand(Command):
    command = "cb"
    usage = "[new binary path]"
    help = "\tChange binary."

    def set_option(self, option, cmd):
        option.binPath = cmd[1]
