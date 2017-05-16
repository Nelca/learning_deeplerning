import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_cnn_init_1":
            self.runsource("print(hint_cnn_init_1)")
            ri = ""
       elif replaced_ri == "hint_cnn_init_2":
            self.runsource("print(hint_cnn_init_2)")
            ri = ""
       elif replaced_ri == "hint_cnn_init_3":
            self.runsource("print(hint_cnn_init_3)")
            ri = ""
       elif replaced_ri == "hint_cnn_predict":
            self.runsource("print(hint_cnn_predict)")
            ri = ""
       elif replaced_ri == "hint_cnn_loss":
            self.runsource("print(hint_cnn_loss)")
            ri = ""
       elif replaced_ri == "hint_cnn_accuracy":
            self.runsource("print(hint_cnn_accuracy)")
            ri = ""
       elif replaced_ri == "hint_cnn_ng":
            self.runsource("print(hint_cnn_ng)")
            ri = ""
       elif replaced_ri == "hint_cnn_save_params":
            self.runsource("print(hint_cnn_save_params)")
            ri = ""
       elif replaced_ri == "hint_cnn_load_param":
            self.runsource("print(hint_cnn_load_param)")
            ri = ""
       return ri

ch07_2_console = CustomConsole(question_file= "./ch07_2_functions.py")
ch07_2_console.interact("### welcome chapter 7-2 !!! ###")

