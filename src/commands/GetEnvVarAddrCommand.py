#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Option import BinType
from Output import Output
from Color import Color
import subprocess


class GetEnvVarAddrCommand(Command):
    command = "geva"
    usage = "[variable name]"
    output = Output()
    help = "\tGet address of an environment variable.\n\tex:\tgeva SHELL"

    def set_option(self, option, cmd):

        cm = ""
        for name, value in option.env.items():
            cm += 'export ' + name + '=' + '`python -c \'print "' + value + '"\'`;'

        if option.binType == BinType.THIRTY_TWO:
            getenv = "../utils/getenv32"
        else:
            getenv = "../utils/getenv64"

        try:
            addr = int(subprocess.check_output(cm + getenv + ' ' + cmd[1], shell=True), 16)
        except Exception:
            self.output.write_error_message("Env variable " + cmd[1] + " not Found")
            return

        addr += len(getenv) - len(option.binPath)

        self.output.write_message("Env variable " + cmd[1] + " Found at " + Color.blue + hex(addr) + Color.reset)
