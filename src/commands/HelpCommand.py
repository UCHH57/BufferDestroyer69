from src.CommandInterface import CommandInterface


class HelpCommand(CommandInterface):
    command = "help"

    def get_command(self):
        return self.command

    def set_option(self, option):
        pass