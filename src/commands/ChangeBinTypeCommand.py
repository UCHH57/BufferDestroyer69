#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Option import BinType


class ChangeBinTypeCommand(Command):
    command = "cbt"
    usage = "[32 | 64]"
    help = "\tChange binary type. (32bit or 64bit)"

    def set_option(self, option, cmd):

        if cmd[1] == "32":
            option.binType = BinType.THIRTY_TWO
        elif cmd[1] == "64":
            option.binType = BinType.SIXTY_FOUR
