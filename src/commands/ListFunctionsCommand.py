#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class ListFunctionsCommand(Command):
    command = "lf"
    help = "\tList functions of the binary."

    def set_option(self, option, cmd):
        system("nm " + option.binPath + " | grep \" T \" | cut -d' ' -f3")
