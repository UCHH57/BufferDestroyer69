import abc


class CommandInterface(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get_command(self):
        pass

    @abc.abstractclassmethod
    def set_option(self, option):
        pass
