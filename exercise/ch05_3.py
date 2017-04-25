import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_network":
            self.runsource("print(hint_network)")
            ri = ""
       elif replaced_ri == "hint_epoch":
            self.runsource("print(hint_epoch)")
            ri = ""
       elif replaced_ri == "hint_batch_mask":
            self.runsource("print(hint_batch_mask)")
            ri = ""
       elif replaced_ri == "hint_grad":
            self.runsource("print(hint_grad)")
            ri = ""
       return ri

ch05_console = CustomConsole(question_file= "./ch05_3_functions.py")
ch05_console.interact("### welcome chapter 5-3 !!! ###")

