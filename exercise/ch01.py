import os
import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        if ri == "import numpy as np":
            print("")
            print("Nice!!")
            print("So next step is type this")
            print("a = np.array([1, 2])")
            print("b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("")
        elif ri == "b = np.array([[1, 2, 3], [4, 5, 6]])" or ri == "b=np.array([[1,2,3],[4,5,6]])" :
            print("")
            print("Gooood!")
            print("Check the define array")
            print("type this ->")
            print("checkArray(a, b)")
            print("")
        elif ri == "b":
            print("")
            print("Good!")
            print("Checking calc result above.")
            print("")
            print("And type this")
            print("b + 3")
            print("")
        elif ri == "b + 3":
            print("")
            print("Nice!")
            print("So next step is type this ->")
            print("b - 3")
            print("")
        elif ri == "b - 3":
            print("")
            print("That's it!")
            print("So next step is type this ->")
            print("c = np.dot(a, b)")
            print("")
        elif ri == "c = np.dot(a, b)":
            print("")
            print("OK.")
            print("next is type this ->")
            print("c")
            print("")
        elif ri == "c":
            print("")
            print("Nice")
            print("")
        return ri

ch01_console = CustomConsole(question_file=os.path.join(os.path.dirname(__file__), "ch01_functions.py"))
ch01_console.interact("### welcome chapter 1 ###")
