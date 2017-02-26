import os
import myconsole as mc


class orMc(mc.MyConsole):
    def check_input(self, ri):
        if ri == "test":
            print("OK!")
        elif ri == "chk1":
            rslt = self.check_result_1(ri)
            print("OK!")

    def check_result_1(self, ri):
        if ri == "chk1":
            print("checked_input")
        else :
            print("check NG...")



or_my_console = orMc(question_file=os.path.join(os.path.dirname(__file__), "runsource_test.py"))
or_my_console.interact("### welcome override console!!! ###")
