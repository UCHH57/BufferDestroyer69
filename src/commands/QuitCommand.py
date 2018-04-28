#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Command import Command


class QuitCommand(Command):
    command = "quit"
    help = "\tExit THE BufferDestroyer69."

    def set_option(self, option, cmd):
        exit(0)
