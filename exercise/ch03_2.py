import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if replaced_ri == "a=np.array([1,2])":
            print("")
        elif replaced_ri == "np.sum(chk)":
            print("")
            self.runsource(ri)
            ri = ""
            print("")
        return ri

ch03_2_console = CustomConsole(question_file= "./ch03_2_functions.py")
ch03_2_console.interact("### welcome chapter 3-2 !!! ###")

