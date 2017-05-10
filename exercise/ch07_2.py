import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_cnn_init":
            self.runsource("print(hint_cnn_init)")
            ri = ""
       elif replaced_ri == "hint_cnn_predict":
            self.runsource("print(hint_cnn_predict)")
            ri = ""
       return ri

ch07_2_console = CustomConsole(question_file= "./ch07_2_functions.py")
ch07_2_console.interact("### welcome chapter 7-2 !!! ###")

