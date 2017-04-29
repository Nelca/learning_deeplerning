import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_momentum":
            self.runsource("print(hint_momentum)")
            ri = ""
       elif replaced_ri == "hint_nesterov":
            self.runsource("print(hint_nesterov)")
            ri = ""
       return ri

ch05_console = CustomConsole(question_file= "./ch06_functions.py")
ch05_console.interact("### welcome chapter 6 !!! ###")

