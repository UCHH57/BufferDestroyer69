#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Output import Output
from Color import Color
from commands.QuitCommand import QuitCommand
from commands.ChangeBinaryCommand import ChangeBinaryCommand
from commands.ChangeModeCommand import ChangeModeCommand
from commands.ChangeShellcodeCommand import ChangeShellcodeCommand
from commands.ListFilesCommand import ListFilesCommand
from commands.ListFunctionsCommand import ListFunctionsCommand
from commands.DisassFunctionsCommand import DisassFunctionsCommand
from commands.CheckASLRCommand import CheckASLRCommand
from commands.JumpToFunctionCommand import JumpToFunctionCommand
from commands.ChangeBufferSizeCommand import ChangeBufferSizeCommand
from commands.SetVariableValueCommand import SetVariableValueCommand
from commands.FindFunctionsCommand import FindFunctionsCommand
from commands.FindStringCommand import FindStringCommand
from commands.ChangeBinTypeCommand import ChangeBinTypeCommand
from commands.JumpToShellcodeCommand import JumpToShellcodeCommand
from commands.RunPayloadCommand import RunPayloadCommand
from commands.SetEnvCommand import SetEnvCommand
from commands.UnSetEnvCommand import UnSetEnvCommand
from commands.GetEnvVarAddrCommand import GetEnvVarAddrCommand
from commands.GDBCommand import GDBCommand
from commands.GetBufferAddrCommand import GetBufferAddrCommand
from commands.NopSpreadCommand import NopSpreadCommand
from commands.FileCommand import FileCommand


class CommandHandler:
    commands = []
    output = Output()

    def __init__(self):
        self.init_all_command()

    def init_all_command(self):
        self.commands.append(QuitCommand())
        self.commands.append(ChangeBinaryCommand())
        self.commands.append(ChangeModeCommand())
        self.commands.append(ChangeShellcodeCommand())
        self.commands.append(ListFilesCommand())
        self.commands.append(ListFunctionsCommand())
        self.commands.append(DisassFunctionsCommand())
        self.commands.append(CheckASLRCommand())
        self.commands.append(JumpToFunctionCommand())
        self.commands.append(ChangeBufferSizeCommand())
        self.commands.append(SetVariableValueCommand())
        self.commands.append(FindFunctionsCommand())
        self.commands.append(FindStringCommand())
        self.commands.append(ChangeBinTypeCommand())
        self.commands.append(JumpToShellcodeCommand())
        self.commands.append(RunPayloadCommand())
        self.commands.append(SetEnvCommand())
        self.commands.append(UnSetEnvCommand())
        self.commands.append(GetEnvVarAddrCommand())
        self.commands.append(GDBCommand())
        self.commands.append(GetBufferAddrCommand())
        self.commands.append(NopSpreadCommand())
        self.commands.append(FileCommand())

    def command_handler(self, cmd, option):

        if cmd[0] == "help":
            for command in self.commands:
                self.output.write_message(Color.purple + command.get_command() +
                                          ":" + " " * (10 - len(command.get_command())) + Color.reset, end='')
                self.output.write_message(Color.pink + command.get_usage() + Color.reset)
                self.output.write_message(command.get_help(), end="\n\n")
            return

        for command in self.commands:
            if cmd[0] == command.get_command():
                try:
                    command.set_option(option, cmd)
                except Exception as ex:
                    print(ex)
                    self.output.write_error_message("usage: " + cmd[0] + ' ' + command.get_usage())
