import os
import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def run_and_clear_source(self, ri):
        self.runsource(ri)
        ri = ""
        return ri
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if ri == "import numpy as np":
            print("")
            print("Nice!!")
            print("So next step is type this")
            print("a = np.array([1, 2])")
            print("b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("")
        elif replaced_ri == "b=np.array([[1,2,3],[4,5,6]])" :
            self.runsource(ri)
            print("")
            print("Gooood!")
            print("Now define variables.")
            print("Check the define array...")
            self.runsource("checkArray(a, b)")
            print("")
        elif replaced_ri == "b":
            ri = self.run_and_clear_source(ri)
            print("")
            print("Good!")
            print("Checking calc result above.")
            print("")
            print("And type this")
            print("b + 3")
            print("")
        elif replaced_ri == "b+3":
            self.runsource(ri)
            ri = ""
            print("")
            print("Nice!")
            print("So next step is type this ->")
            print("b - 3")
            print("")
        elif replaced_ri == "b-3":
            self.runsource(ri)
            ri = ""
            print("")
            print("That's it!")
            print("So next step is type this ->")
            print("c = np.dot(a, b)")
            print("")
        elif replaced_ri == "c=np.dot(a,b)":
            print("")
            print("OK.")
            print("Lete's view the result.")
            print("next is type this ->")
            print("c")
            print("")
        elif ri == "c":
            self.runsource(ri)
            ri = ""
            print("")
            print("Nice")
            print("Next is array flatten convert.")
            print("")
            print("Type this ->")
            print("b.flatten()")
            print("")
        elif ri == "b.flatten()":
            self.runsource(ri)
            ri = ""
            print("")
            print("Good.")
            print("b.flatten() convert a multidemensional array to one-demensional array.")
            print("")
            print("Next lean about boolean judgement.")
            print("")
            print("Type this ->")
            print("b > 3")
            print("")
        elif replaced_ri == "b>3":
            self.runsource(ri)
            ri = ""
            print("")
            print("Nice.")
            print("")
            print("OK, let's move next chapter.")
            self.runsource("nextChapter()")
            print("")
        return ri

ch01_console = CustomConsole(question_file=os.path.join(os.path.dirname(__file__), "ch01_functions.py"))
ch01_console.interact("### welcome chapter 1 ###")
