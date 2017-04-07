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
       elif replaced_ri == "net=simpleNet()":
            self.runsource(ri)
            ri = ""
            print("Okay, next is check the net.")
            print("")
            print("First of all view net weight.")
            print("print(net.W)")
            print("")
       elif replaced_ri == "print(net.W)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Grate!")
            print("This is the simple net weight.")
            print("And next is predict.")
            print("define input and execute predict of simple net as follow.")
            print("")
            print("x = np.array([0.6, 0.9])")
            print("p = net.predict(x)")
            print("print(p)")
       elif replaced_ri == "view_simple_net":
            self.runsource("print(view_simple_net)")
            ri = ""
       elif replaced_ri == "print(p)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Tha's good!")
            print("and calc index of max value as follow.")
            print("np.argmax(p)")
            print("")
       elif replaced_ri == "np.argmax(p)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Okay, next is define collect label as follow.")
            print("t = np.array([0, 0, 1])")
            print("")
       elif replaced_ri == "t=np.array([0,0,1])":
            self.runsource(ri)
            ri = ""
            print("That's it!")
            print("and calc loss as follow.")
            print("net.loss(x, t)")
            print("")
       elif replaced_ri == "net.loss(x,t)":
            self.runsource(ri)
            ri = ""
            print("That's good!!!")
            print("Next is calcurate gradient as below.")
            print("")
            print("Nnow use the dummy function as follow.")
            print("dummy_f = lambda w: net.loss(x, t)")
            print("")
            print("So you can calcurate gradient as follow.")
            print("")
            print("dW = numerical_gradient(dummy_f, net.W)")
            print("print(dW)")
            print("")
       elif replaced_ri == "print(dW)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Yeah!!")
            print("It's calucurated answer is gradient.")
            print("")
            print("Next is difine lerning algorism.")
            print("Lerning neural net is 4step.")
            print("1.minibatch")
            print("2.calcurate gradient")
            print("3.update parameter")
            print("4.iterate")
            print("")
            print("Now check two layer net.")
            print("This nueral net class is defined as 'TwoLayerNet'.")
            print("But it's not a perfect.")
            print("So, you define this net's param etc.")
            print("")
            print("First of all, define weight of this net like this")
            print("tlNet.params['W1'] = foo")
            print("")
            print("")
            print("And check the param as follow")
            print("checkTlnetParam(tlNet)")
       elif replaced_ri == "hint_grad_desc":
            self.runsource("print(hint_grad_desc)")
            ri = ""
       elif replaced_ri == "hint_weight_param":
            self.runsource("print(hint_weight_param)")
            ri = ""
       elif replaced_ri == "hint_bias_param":
            self.runsource("print(hint_bias_param)")
            ri = ""
       elif replaced_ri == "y=net.predict(dummy_x)" or ri == "next_predict":
            if replaced_ri == "y=net.predict(dummy_x)":
                self.runsource(ri)
            ri = ""
            self.runsource("print(y)")
            print("")
            print("Okay, predict result is abobe.")
            print("Next is calcurate network")
            print("")
            print("Calcurate program is as follow.")
            print("So, you fill in the hole filling questioin.")
            print("")
            self.runsource("print(question_train_tl_net)")
            print("")
            print("Define your answer as follow.")
            print("question_1 = foo")
            print("question_2 = bar")
            print("question_3 = baz")
            print("")
            print("And, check your answer as follow.")
            print("checkTrainAns()")
       elif replaced_ri == "hint_train_ans":
            self.runsource("print(hint_train_ans)")
            ri = ""
       return ri

ch04_2_console = CustomConsole(question_file= "./ch04_2_functions.py")
ch04_2_console.interact("### welcome chapter 4-2 !!! ###")

