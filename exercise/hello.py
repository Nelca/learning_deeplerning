import os
import myconsole as mc


class Mc(mc.MyConsole):
    def check_input(self, ri):
        if ri == "import numpy as np":
            print("OK!")
            print("now, nmpy is avvaiabble")
        elif ri == "chk1":
            print("OK!")

    def check_result_1(self, ri):
        if ri == "chk1":
            print("checked_input")
        else :
            print("check NG...")



hello_my_console = Mc(question_file=os.path.join(os.path.dirname(__file__), "hello_python.py"))
hello_my_console.interact("### welcome python !!! ###")
