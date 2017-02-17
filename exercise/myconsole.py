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
            histfile=os.path.expanduser("~/.console-history"),
            run_source_file=os.path.expanduser("runsource_test.py")):
        code.InteractiveConsole.__init__(self, local, filename)
        code.InteractiveConsole.runsource(self, source=run_source_file)
        self.init_history(histfile)
        self.check_function()

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

    def check_function(self):
        print("check_function")


my_console = MyConsole()
my_console.interact("### welcome to my console!!! ###")

