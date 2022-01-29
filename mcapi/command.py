from shlex import split

from cloudburst.pythonaddon import PythonSystem


class Command(object):
    
    def init(self, name, description="Python command."):
        PythonSystem.INSTANCE.pycommands.append(self)
        self.name = name
        self.description = description
        
    def parse_args(self, argstr):
        return split(argstr)
    
    def execute_command(self, args=""):
        self.command(*self.parse_args(args))
    
    def command(self):
        pass