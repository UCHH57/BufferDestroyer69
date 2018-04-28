#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command
from os import system


class FileCommand(Command):
    command = "f"
    help = "\tGet file type of the binary."

    def set_option(self, option, cmd):
        system("file " + option.binPath)
