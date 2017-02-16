import myconsole as mc


class orMc(mc.MyConsole):
    def check_input(self, ri):
        if ri == "test":
            print("OK!")

or_my_console = orMc()
or_my_console.interact("### welcome override console!!! ###")
