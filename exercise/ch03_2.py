import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if replaced_ri == "x,t=get_data()":
            print("")
            print("Nice.")
            print("this variable data is")
            print("x:is train data")
            print("t:is test data")
            print("")
            print("So checking the mnist datas.")
            print("")
            print("")
            print("")
        elif replaced_ri == "np.sum(chk)":
            print("")
            self.runsource(ri)
            ri = ""
            print("")
        return ri

ch03_2_console = CustomConsole(question_file= "./ch03_2_functions.py")
ch03_2_console.interact("### welcome chapter 3-2 !!! ###")

