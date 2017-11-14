#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.Option import Mode, Option
from os import system


class ExecInstruction:
    option = None

    def __init__(self, option):
        self.option = option

    def run(self, payload):

        if self.option:

            if self.option.execMode == Mode.PIPED:
                system("python -c 'import sys; sys.stdout.write(\"" + payload + "\")' | " + option.binPath)

            elif self.option.execMode == Mode.ARG:
                system(option.binPath + ' ' + payload)


if __name__ == '__main__':
    """
        Unit Test
    """
    option = Option("../test/testArg")
    option.execMode = Mode.ARG
    execInstruction = ExecInstruction(option)

    execInstruction.run("test")

    option.binPath = "../test/testPiped"
    option.execMode = Mode.PIPED

    execInstruction.run("test")
