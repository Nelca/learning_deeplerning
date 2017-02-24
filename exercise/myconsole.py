#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import sys
import code
import readline
import atexit
import os

class MyConsole(code.InteractiveConsole):

    def __init__(self, local=None, filename="<console>",
            histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, local, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.write_history_file(histfile)

    def raw_input(self, prompt):
        ri = code.InteractiveConsole.raw_input(self, prompt)
        self.check_input(ri)
        return ri

    def check_input(self, ri):
        if ri == "hey":
            print("YO!")

my_console = MyConsole()

f = open('runsource_test.py')
lines = f.readlines()
f.close()

str_source = ""
i = 0
for line in lines:
    i = i + 1
    print(line)
    print(i)
    str_source = str_source + line

#my_console.runsource(str_source)
#my_console.runsource("def test_func():    print('check_rs')")
#my_console.runsource("test_func()")

#my_console.runsource("import runsource_test as rt")
my_console.interact("### welcome to my console!!! ###")

