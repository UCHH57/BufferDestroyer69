#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.CommandInterface import CommandInterface


class HelpCommand(CommandInterface):
    command = "help"

    def get_command(self):
        return self.command

    def set_option(self, option):
        pass
