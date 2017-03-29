import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_ce_error":
            self.runsource("print(hint_ce_error)")
            ri = ""
       elif replaced_ri == "hint_random_data":
            self.runsource("print(hint_random_data)")
            ri = ""
       return ri

ch04_2_console = CustomConsole(question_file= "./ch04_2_functions.py")
ch04_2_console.interact("### welcome chapter 4-2 !!! ###")

