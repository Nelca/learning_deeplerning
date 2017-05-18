import numpy as np

##########   questions and hints   ##############
view_predict = """
def predict(self, x, train_flg=False):
    for layer in self.layers:
        if question_1:
            x = question_2
        else:
            x = question_3
    return x
"""

hint_predict = """
predict answers is as follow.

question_1 = isinstance(layer, Dropout)
question_2 = layer.forward(x, train_flg)
question_3 = layer.forward(x)



And check your answer as follow.
checkDCNPredict()
"""

view_gradient = """
def gradient(self, x, t):
    # forward
    self.loss(x, t)

    # backward
    dout = 1
    dout = self.last_layer.backward(dout)

    tmp_layers = self.layers.copy()
    tmp_layers.reverse()
    for layer in tmp_layers:
        dout = layer.backward(dout)

    # configulation
    grads = {}
    for i, layer_idx in enumerate((0, 2, 5, 7, 10, 12, 15, 18)):
        grads['W' + str(i+1)] = self.layers[layer_idx].dW
        grads['b' + str(i+1)] = self.layers[layer_idx].db

    return grads
"""



#############################################

##########   inital message   ##############
print("*****************************")
print("")
print("Last chpater is Lerning Deep lerning.")
print("Let's define Deep Convolutional Network.")
print("Network is as follow.")
print("")
print("conv - relu - conv- relu - pool -")
print("conv - relu - conv- relu - pool -")
print("conv - relu - conv- relu - pool -")
print("affine - relu - dropout - affine - dropout - softmax")
print("")
print("init function is so complecated, so define predict function.")
print("")
print(view_predict)
print("")
print("And check your answer as follow.")
print("checkDCNPredict")
#############################################


##########   answers   ##############

ans_predict_1 = isinstance(layer, Dropout)
ans_predict_2 = layer.forward(x, train_flg)
ans_predict_3 = layer.forward(x)

#############################################


##########   answer check functions   ##############

def checkDCNPredict():
    chk_1 = ans_predict_1==question_1
    chk_2 = ans_predict_2==question_2
    chk_3 = ans_predict_3==question_3
    if chk_1 and chk_2 and chk_3 :
        print("Goood!!!")
        print("Loss, accuracy functions is skipped.")
        print("So next is gradient")
        print("")
        print(view_gradient)
        print("")
        print("Fill in your answer and check as follow.")
        print("checkDCNGradient()")
    else:
        print("Mmmmm... your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_predict")
        print("")
        print("And check your answer as follow.")
        print("checkDCNPredict()")


def checkDCNGradient():
    chk_1 = 
    if chk_1 :
        print("")
        print("")
        print("")
    else:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")


#############################################


##########   nest chapter function   ##############
def nextChapter(file_name="ch07_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

