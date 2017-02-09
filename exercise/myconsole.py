import sys
import code

class MyConsole(code.InteractiveConsole):
    def __init__(self, local=None, filename="<console>"):
        code.InteractiveConsole.__init__(self, local,  filename)

    def push(self, line):
        if line == "minato":
            print("Hi!!!")

my_console = MyConsole()
sys.ps1 = "c>>>"
sys.ps2 = "----->>>"
my_console.interact("Welcome to mylife")

