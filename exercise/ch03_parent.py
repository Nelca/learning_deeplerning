import os
import myconsole as mc


class Mc(mc.MyConsole):
    def check_input(self, ri):
        if ri == "import numpy as np":
            print("Good !! Now numpy is avaiabble.")
            print("So let's do next step is")
            print("type this-> a = np.array([1, 2])")
            print("and type this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("and type this->checkArray(a, b) ")
        elif ri == "print(a)":
            print("That's it.")
            print("So next type this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
        elif ri == "sig_a = np.array([1, 2, 3])":
            print("That's it.")
            print("So next type this-> sig_a_exp = np.exp(sig_a_exp)")
        elif ri == "sig_a_exp = np.exp(sig_a_exp)":
            print("Good good good.")
            print("print(a_exp)")

    def check_result_1(self, ri):
        if ri == "chk1":
            print("checked_input")
        else :
            print("check NG...")



hello_my_console = Mc(question_file=os.path.join(os.path.dirname(__file__), "ch03.py"))
hello_my_console.interact("### welcome python !!! ###")
