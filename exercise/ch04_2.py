import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
       replaced_ri = ri.replace(" ", "")
       if ri == "hint_nu_diff":
            self.runsource("print(hint_nu_diff)")
            ri = ""
       elif replaced_ri == "hint_random_data":
            self.runsource("print(hint_random_data)")
            ri = ""
       elif replaced_ri=="numerical_gradient(chk_function_2,np.array([3.0,4.0]))" or ri=="next_of_gradient_chk":
            self.runsource(ri)
            ri = ""
            print("")
            print("OK!!!")
            print("It's a one of result of chk_function_2.")
            print("")
            print("Next we will learn about the gradient descent method.")
            print("So, define the gradient descent function as follow.")
            print("def gradient_descent(f, init_x, lr=0.01, step_num=100):")
            print(".....")
            print("")
            print("And check your defined function as follow.")
            print("checkGradDesc()")
            print("")
            print("If you want a hint type this->")
            print("hint_grad_desc")
       elif replaced_ri == "hint_grad_desc":
            self.runsource("print(hint_grad_desc)")
            ri = ""
       return ri

ch04_2_console = CustomConsole(question_file= "./ch04_2_functions.py")
ch04_2_console.interact("### welcome chapter 4-2 !!! ###")

