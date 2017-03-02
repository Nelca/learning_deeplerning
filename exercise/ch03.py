import os
import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        if ri == "sig_a = np.array([1, 2, 3])":
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
        return ri

ch03_console = CustomConsole(question_file=os.path.join(os.path.dirname(__file__), "ch03_functions.py"))
ch03_console.interact("### welcome chapter 3 !!! ###")

