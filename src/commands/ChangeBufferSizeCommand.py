#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class ChangeBufferSizeCommand(Command):
    command = "cbs"
    usage = "[size]"
    help = "\tChange buffer size.\n\tex:\tcbs 128"

    def set_option(self, option, cmd):
        option.buffSize = int(cmd[1])
