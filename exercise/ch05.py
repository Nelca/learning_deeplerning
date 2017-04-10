import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_ml_forword":
            self.runsource("print(hint_nu_diff)")
            ri = ""
       elif replaced_ri == "hint_random_data":
            self.runsource("print(hint_random_data)")
            ri = ""
       return ri

ch05_console = CustomConsole(question_file= "./ch05_functions.py")
ch05_console.interact("### welcome chapter 5 !!! ###")

