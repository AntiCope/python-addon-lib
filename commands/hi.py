import mcapi
from mcapi.utils import chat

class HiCommand(mcapi.Command):
    def __init__(self):
        self.init("hi", "Hi command.")

    def command(self, name):
        chat.info("Hi, ", name, "!")

py = HiCommand()
