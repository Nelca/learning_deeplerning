import customconsole as cc

class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if replaced_ri == "hint_and_gate" :
           print("")
           print("and gate is")
           print("")
           print("def AND(x1, x2):")
           print("    x = np.array([x1, x2])")
           print("    w = np.array([0.5, 0.5])")
           print("    b = -0.7")
           print("    tmp = np.sum(w*x) + b")
           print("    if tmp <= 0:")
           print("        return 0")
           print("    else:")
           print("        return 1")
           ri = ""
        elif replaced_ri == "hint_nand_gate" :
           print("")
           print("OK! Give you a hint.")
           print("")
           print("NAND gate is ->")
           print("")
           print("def NAND(x1, x2):")
           print("   x = np.array([x1, x2])")
           print("   w = np.array([-0.5, -0.5])")
           print("   b = 0.7")
           print("   tmp = np.sum(w*x) + b")
           print("   if tmp <= 0:")
           print("       return 0")
           print("   else:")
           print("       return 1")
           ri = ""
        elif replaced_ri == "hint_or_gate" :
           print("")
           print("OK! Give you a hint.")
           print("")
           print("OR gate is ->")
           print("")
           print("def OR(x1, x2):")
           print("    x = np.array([x1, x2])")
           print("    w = np.array([0.5, 0.5])")
           print("    b = -0.2")
           print("    tmp = np.sum(w*x) + b")
           print("    if tmp <= 0:")
           print("        return 0")
           print("    else:")
           print("        return 1")
           ri = ""
        elif replaced_ri == "hint_xor_gate" :
           print("")
           print("XOR gate is ->")
           print("")
           print("def XOR(x1, x2):")
           print("    s1 = NAND(x1, x2)")
           print("    s2 = OR(x1, x2)")
           print("    y = AND(s1, s2)")
           print("    return y")
           ri = ""
        return ri

ch02_console = CustomConsole(question_file="./ch02_functions.py")
ch02_console.interact("### welcome chapter 2 ###")
