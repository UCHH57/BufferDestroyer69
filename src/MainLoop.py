#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from CommandHandler import CommandHandler
from UserInput import UserInput
from Output import Output
from Option import Option
from ExecInstruction import ExecInstruction
from Color import Color


class MainLoop:
    option = Option()
    quit = False
    userInput = UserInput()
    commandHandler = CommandHandler()
    output = Output()
    execInstrution = ExecInstruction()

    def __init__(self, option):
        self.option = option
        self.start_loop()

    def start_loop(self):
        while not self.quit:
            self.output.load_prompt()
            try:
                cmd = self.userInput.read_input()

                if cmd:
                    self.option.payload = None
                    self.commandHandler.command_handler(cmd, self.option)

                    if self.option.payload:
                        self.execInstrution.run(self.option)

            except KeyboardInterrupt:
                self.output.write_message("use " + Color.pink + "\"quit\"" + Color.reset + " to exit")
