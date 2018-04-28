#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Option import Mode


class ChangeModeCommand(Command):
    command = "cm"
    usage = "[piped | arg]"
    help = "\tChange binary execution mode.\n\targ:\t./vulnBin payload\n\tpiped:\techo payload | ./vulnBin"

    def set_option(self, option, cmd):

        if cmd[1] == "piped":
            option.execMode = Mode.PIPED
        elif cmd[1] == "arg":
            option.execMode = Mode.ARG
