#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from Option import Mode
from Output import Output
from os import system
import subprocess


class GetBufferAddrCommand(Command):
    command = "gba"
    output = Output()
    help = "\tGet potential buffer address. (for Nop spread)"

    def set_option(self, option, cmd):

        r = "0x0"

        cm = ""
        for name, value in option.env.items():
            cm += 'export ' + name + '=' + '`python -c \'print "' + value + '"\'`;'

        res = subprocess.check_output(cm + "echo \"disass main\" | gdb " + option.binPath + " | grep ret",
                                      shell=True).decode().split(' ')
        for r in res:
            if r.startswith("0x"):
                break

        p = subprocess.run(['gdb'], stdout=subprocess.PIPE, input='q\n', encoding='ascii')

        if p.stdout.split('\n')[-1].find('peda') != -1:

            if option.execMode == Mode.PIPED:
                system("echo BUFFER69 > tmp")
                system(cm + "(echo 'b *" + r + "'; echo 'r < tmp'; echo 'find BUFFER69') | gdb " +
                       option.binPath + " 2>/dev/null | awk '/Searching/{f=1;next} /quit/{f=0} f'")
                system("rm tmp")
            else:
                system(cm + "(echo 'b *" + r + "'; echo 'r BUFFER69'; echo 'find BUFFER69') | gdb " +
                       option.binPath + " 2>/dev/null | awk '/Searching/{f=1;next} /quit/{f=0} f'")
        else:
            self.output.write_error_message("gdp-peda required for this cmd.")
