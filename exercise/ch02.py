import os
import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if ri == "import numpy as np":
            print("")
        elif replaced_ri == "b=np.array([[1,2,3],[4,5,6]])" :
           print("")
           print("")
        elif replaced_ri == "hint_and_gate" :
           print("")
           print("and gate is")
           print("")
           print("def AND(x1, x2):")
           print("    x = np.array([x1, x2])")
           print("    w = np.array([0.5, 0.5])")
           print("    b = -0.7")
           print("    tmp = np.sum(w*x) + b")
           print("    if tmp <= 0:")
           print("        return 0")
           print("    else:")
           print("        return 1")
           print("")
           print("")
        elif replaced_ri == "hint_nand_gate" :
           print("")
           print("Nand gate is ->")
           print("")
           print("")
           print("")
           print("")
           print("")
           print("")
           print("")
           print("")
           print("")
        return ri

ch02_console = CustomConsole(question_file="./ch02_functions.py")
ch02_console.interact("### welcome chapter 2 ###")
