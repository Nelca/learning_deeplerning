import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_ml_forward":
            self.runsource("print(hint_ml_forward)")
            ri = ""
       elif replaced_ri == "hint_ml_backward":
            self.runsource("print(hint_ml_backward)")
            ri = ""
       elif replaced_ri == "hint_relu_forward":
            self.runsource("print(hint_relu_forward)")
            ri = ""
       elif replaced_ri == "hint_relu_backward":
            self.runsource("print(hint_relu_backward)")
            ri = ""
       return ri

ch05_console = CustomConsole(question_file= "./ch05_functions.py")
ch05_console.interact("### welcome chapter 5 !!! ###")

