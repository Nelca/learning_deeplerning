import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_im2col":
            self.runsource("print(hint_im2col)")
            ri = ""
       elif replaced_ri == "view_im2col":
            self.runsource("print(view_im2col)")
            ri = ""
       elif replaced_ri == "hint_conv":
            self.runsource("print(hint_conv)")
            ri = ""
       return ri

ch07_console = CustomConsole(question_file= "./ch07_functions.py")
ch07_console.interact("### welcome chapter 7 !!! ###")

