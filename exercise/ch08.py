import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_predict":
            self.runsource("print(hint_predict)")
            ri = ""
       elif replaced_ri == "hint_gradient":
            self.runsource("print(hint_gradient)")
            ri = ""
       return ri

ch08_console = CustomConsole(question_file= "./ch08_functions.py")
ch08_console.interact("### welcome chapter 8 !!! ###")

