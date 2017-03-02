#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import sys
import code
import readline
import atexit
import os

class CustomConsole(code.InteractiveConsole):

    def __init__(self, local=None, filename="<console>",
            histfile=os.path.expanduser("~/.console-history"),
            question_file=os.path.join(os.path.dirname(__file__), "empty_question_file.py")):

        code.InteractiveConsole.__init__(self, local, filename)

        self.init_history(histfile)

        f = open(question_file)
        self.runsource(f.read(), symbol='exec')
        f.close()

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
        return self.check_input(ri)

    def check_input(self, ri):
        if ri == "hey":
            print("YO!")
        return ri

