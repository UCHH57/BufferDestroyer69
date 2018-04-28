#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class ListFilesCommand(Command):
    command = "ls"
    help = "\tList files of a directory."

    def set_option(self, option, cmd):
        args = ""
        for arg in cmd:
            if arg != "ls":
                args = args + " " + arg
        system("ls -F " + args)
