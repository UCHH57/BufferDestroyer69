#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .CommandHandler import CommandHandler
from .UserInpout import UserInput
from .Output import Output
from .Option import Option


class MainLoop:
    option = Option
    quit = False
    userInput = UserInput()
    commandHandler = CommandHandler()
    output = Output()

    def __init__(self, option):
        self.option = option
        self.start_loop()

    def start_loop(self):
        while not self.quit:
            self.output.load_prompt()
            cmd = self.userInput.read_input()
            self.commandHandler.command_handler(cmd, self.option)
