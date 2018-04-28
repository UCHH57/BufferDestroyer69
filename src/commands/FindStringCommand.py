#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system
from subprocess import run, PIPE


class FindStringCommand(Command):
    command = "fs"
    usage = "[string]"
    help = "\tFind a specific string in memory.\n\tex:\tfs /bin/sh"

    def set_option(self, option, cmd):

        cm = ""
        for name, value in option.env.items():
            cm += 'export ' + name + '=' + '`python -c \'print "' + value + '"\'`;'

        p = run(['gdb'], stdout=PIPE, input='q\n', encoding='ascii')

        if p.stdout.split('\n')[-1].find('peda') != -1:

            cm += "(echo 'b main'; echo 'r'; echo 'find " + cmd[1] + "') | gdb "
            cm += option.binPath + " 2>/dev/null | awk '/Searching/{f=1;next} /quit/{f=0} f'"
        else:
            cm += "(echo 'b main'; echo 'r'; echo 'find __libc_start_main,+99999999,\"" + cmd[1] + "\"') | gdb "
            cm += option.binPath + " 2>/dev/null | awk '/in main/{f=1;next} /quit/{f=0} f'"

        system(cm)
