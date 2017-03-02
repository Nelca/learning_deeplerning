import os
import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        if ri == "test":
            print("check input")
            ri = "hello()"
        elif ri == "test_2":
            print("yeah it's test_2")
        return ri

ch01_console = CustomConsole(question_file=os.path.join(os.path.dirname(__file__), "ch01_functions.py"))
ch01_console.interact("### welcome chapter 1 ###")
