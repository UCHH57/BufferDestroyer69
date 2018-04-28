#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class RunPayloadCommand(Command):
    command = "rp"
    usage = "[payload]"
    help = "\tRun a specific custom payload.\n\tex:\trp \"\\xde\\xad\\xbe\\xef\" * 500"

    def set_option(self, option, cmd):

        if len(cmd) == 1:
            raise Exception('')

        option.payload = ""
        cmd = cmd[1:]

        for arg in cmd:
            option.payload += arg + ' '
