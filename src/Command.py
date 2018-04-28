#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from CommandInterface import CommandInterface


class Command(CommandInterface):
    command = ""
    usage = ""
    help = ""

    def get_command(self):
        return self.command

    def get_usage(self):
        return self.usage

    def get_help(self):
        return self.help

    def set_option(self, option, cmd):
        pass
