#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Option import Mode
from os import system

class ExecInstruction:
    option = None
    binPath = "./a.out"

    def __init__(self, option, binPath):
        self.option = option
        self.binPath = binPath

    def run(self, payload):

        if self.option:

            if self.option.execMode == Mode.PIPED:
                system(payload + ' | ' + self.binPath)

            elif self.option.execMode == Mode.ARG:
                system(self.binPath + ' ' + payload)
