import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        if ri == "hint_sigmoid":
            print("")
            print("Sigmoid function is defined as follows.")
            print("")
            print("1 / (1 + np.exp(-x))")
            print("")
            print("")
        elif ri == "hint_step_func":
            print("")
            print("Step function is this->")
            print("")
            print("def step_function(x):")
            print("    return np.array(x > 0, dtype=np.int)")
            print("")
        elif ri == "hint_ReLU":
            print("")
            print("ReLU is this->")
            print("")
            print("def ReLU(x):")
            print("    return np.maximum(0, x)")
            print("")
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
        return ri

ch03_console = CustomConsole(question_file= "./ch03_functions.py")
ch03_console.interact("### welcome chapter 3 !!! ###")

