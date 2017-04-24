import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if replaced_ri == "hint_tl_init":
            self.runsource("print(hint_tl_init)")
            ri = ""
       elif replaced_ri == "hint_tl_predict":
            self.runsource("print(hint_tl_predict)")
            ri = ""
       elif replaced_ri == "hint_tl_loss":
            self.runsource("print(hint_tl_loss)")
            ri = ""
       elif replaced_ri == "hint_tl_accuracy":
            self.runsource("print(hint_tl_accuracy)")
            ri = ""
       elif replaced_ri == "hint_tl_ng":
            self.runsource("print(hint_tl_ng)")
            ri = ""
       return ri

ch05_console = CustomConsole(question_file= "./ch05_2_functions.py")
ch05_console.interact("### welcome chapter 5-2 !!! ###")

