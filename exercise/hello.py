# This file is chapter 1 exercise.
import os
import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        if ri == "import numpy as np":
            print("Good !! Now numpy is avaiabble.")
            print("So let's do next step is")
            print("type this-> a = np.array([1, 2])")
            print("and type this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("and type this->checkArray(a, b) ")
        elif ri == "print(a)":
            print("That's it.")
            print("")
            print("and type this")
            self.runsource("checkNumpy()")
        elif ri == "sig_a = np.array([1, 2, 3])":
            print("That's it.")
            print("So next type this-> sig_a_exp = np.exp(sig_a_exp)")
        elif ri == "sig_a_exp = np.exp(sig_a_exp)":
            print("Good good good.")
            print("print(a_exp)")
        elif ri == "y":
            print("Is displayed this ? ")
            print("array([False, True, True], dtype=bool)")
            print("So, let's next chapter.")
            print("type this -> nextCh()")
        elif ri == "test":
            self.runsource("checkNumpy()")
        return ri

hello_my_console = CustomConsole(question_file="./hello_functions.py")
hello_my_console.interact("### welcome python !!! ###")
