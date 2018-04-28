#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Option import Mode, Option
from Output import Output
from Color import Color
from os import system


class ExecInstruction:
    output = Output()

    def __init__(self):
        pass

    def run(self, option):

        if option:
            cmd = ""

            for name, value in option.env.items():
                cmd += 'export ' + name + '=' + '`python -c \'print "' + value + '"\'`;'

            if option.execMode == Mode.PIPED:
                cmd += "(python -c 'print(" + option.payload + ")'; cat) | " + option.binPath

            elif option.execMode == Mode.ARG:
                cmd += option.binPath + " `python -c 'import sys; sys.stdout.write(" + option.payload + ")'`"

            if option.bruteforce:
                option.bruteforce = False
                try:
                    while True:
                        self.output.write_message(Color.yellow + "executing command: " + cmd + Color.reset)
                except KeyboardInterrupt:
                    pass

            self.output.write_message(Color.pink + "executing command: " + cmd + Color.reset)
            system(cmd)


if __name__ == '__main__':
    """
        Unit Test
    """
    options = Option("../test/testArg")
    options.execMode = Mode.ARG
    options.payload = "\"test\""
    execInstruction = ExecInstruction()

    execInstruction.run(options)

    options.binPath = "../test/testPiped"
    options.execMode = Mode.PIPED

    execInstruction.run(options)
