from src.CommandInterface import CommandInterface


class QuitCommand(CommandInterface):
    command = "quit"

    def get_command(self):
        return self.command

    def set_option(self, option):
        pass
