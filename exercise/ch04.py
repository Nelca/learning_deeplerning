import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_ms_error":
            print("")
            print("Mean squared error function as follow.")
            print("")
            print("def mean_squared_error(y, t):")
            print("    return 0.5 * np.sum((y-t)**2)")
            print("")
            print("And check your define function as follow.")
            print("checkMsError()")
            ri = ""
       elif ri == "hint_ce_error":
            self.runsource("print(hint_ce_error)")
            ri = ""
       elif ri == "hint_random_data":
            self.runsource("print(hint_random_data)")
            ri = ""
       return ri

ch04_console = CustomConsole(question_file= "./ch04_functions.py")
ch04_console.interact("### welcome chapter 4 !!! ###")

