from CommandHandler import CommandHandler
from UserInpout import UserInput

from src.Output import Output


class MainLoop:
    option = []
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
