from .commands.HelpCommand import HelpCommand
from .commands.QuitCommand import QuitCommand


class CommandHandler:
    commands = []

    def __init__(self):
        self.init_all_command()

    def init_all_command(self):
        self.commands.append(HelpCommand())
        self.commands.append(QuitCommand())


    def command_handler(self, cmd, option):
        for command in self.commands:
            if cmd[0] == command.get_command():
                command.set_option(option)
                print(command.get_command())
