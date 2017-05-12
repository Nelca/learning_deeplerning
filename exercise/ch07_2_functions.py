import numpy as np
import ch07_2_answers

##########   questions and hints   ##############
view_cnn_init_1 = """
filter_num = question_1
filter_size = question_2
filter_pad = question_3
filter_stride = question_4
input_size = question_5
conv_output_size = question_6
pool_output_size = question_7
"""

hint_cnn_init_1 = """
conv init is as follow.

question_1 = conv_param['filter_num']
question_2 = conv_param['filter_size']
question_3 = conv_param['pad']
question_4 = conv_param['stride']
question_5 = input_dim[1]
question_6 = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
question_7 = int(filter_num * (conv_output_size/2) * (conv_output_size/2))

so define the answers, ans check your answer as follow.
checkConvInit()
"""

view_cnn_init_2 = """
self.params = {}
self.params['W1'] = question_1
self.params['b1'] = question_2
self.params['W2'] = question_3
self.params['b2'] = question_4
self.params['W3'] = question_5
self.params['b3'] = question_6
"""

hint_cnn_init_2 = """
conv init is as follow.

question_1 = weight_init_std * np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
question_2 = np.zeros(filter_num)
question_3 = weight_init_std * np.random.randn(pool_output_size, hidden_size)
question_4 = np.zeros(hidden_size)
question_5 = weight_init_std * np.random.randn(hidden_size, output_size)
question_6 = np.zeros(output_size)

so define the answers, ans check your answer as follow.
checkConvInit2()
"""
view_cnn_init_3 = """
self.layers = OrderedDict()
self.layers['Conv1'] = question_1
self.layers['Relu1'] = question_2
self.layers['Pool1'] = question_3
self.layers['Affine1'] = question_4
self.layers['Relu2'] = question_5
self.layers['Affine2'] = question_6

self.last_layer = SoftmaxWithLoss()
"""
hint_cnn_init_3 = """
conv init hints is as follow.

question_1 = Convolution(self.params['W1'], self.params['b1'], conv_param['stride'], conv_param['pad'])
question_2 = Relu()
question_3 = Pooling(pool_h=2, pool_w=2, stride=2)
question_4 = Affine(self.params['W2'], self.params['b2'])
question_5 = Relu()
question_6 = Affine(self.params['W3'], self.params['b3'])

So, define the answers and check your answer as follow.
checkConvInit3()
"""

hint_cnn_predict = """
predict function is as follow.

def predict(self, x):
    for layer in self.layers.values():
        x = layer.forward(x)

    return x

So, check your answer as follow.
checkConvPredict()
"""

hint_cnn_loss = """
convolution loss function is as follow.

def loss(self, x, t):
    y = self.predict(x)
    return self.last_layer.forward(y, t)

So, define the answer and check your answer as follow.
checkConvLoss()
"""




#############################################

##########   inital message   ##############
print("*****************************")
print("")
print("This chpater is implementation of CNN")
print("The CNN layers is ,")
print("conv - relu - pool - affine - relu - affine - softmax")
print("")
print("First step is define cnn initialize.")
print("init arguments is as follow")
print("")
print("self, input_dim=(1, 28, 28), conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}, hidden_size=100, output_size=10, weight_init_std=0.01")
print("")
print(view_cnn_init_1)
print("")
#############################################


##########   answers   ##############

conv_param = {'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}
input_dim=(1, 28, 28)
hidden_size=100
output_size=10
weight_init_std=0.01
input_size = input_dim[1]
filter_num = conv_param['filter_num']
filter_size = conv_param['filter_size']
filter_pad = conv_param['pad']
filter_stride = conv_param['stride']
conv_output_size = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
pool_output_size = int(filter_num * (conv_output_size/2) * (conv_output_size/2))

ans_conv_init_1 = conv_param['filter_num']
ans_conv_init_2 = conv_param['filter_size']
ans_conv_init_3 = conv_param['pad']
ans_conv_init_4 = conv_param['stride']
ans_conv_init_5 = input_dim[1]
ans_conv_init_6 = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
ans_conv_init_7 = int(filter_num * (conv_output_size/2) * (conv_output_size/2))

ans_conv_init2_1 = weight_init_std * np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
ans_conv_init2_2 = np.zeros(filter_num)
ans_conv_init2_3 = weight_init_std * np.random.randn(pool_output_size, hidden_size)
ans_conv_init2_4 = np.zeros(hidden_size)
ans_conv_init2_5 = weight_init_std * np.random.randn(hidden_size, output_size)
ans_conv_init2_6 = np.zeros(output_size)

ans_conv_init3_1 = Convolution(self.params['W1'], self.params['b1'], conv_param['stride'], conv_param['pad'])
ans_conv_init3_2 = Relu()
ans_conv_init3_3 = Pooling(pool_h=2, pool_w=2, stride=2)
ans_conv_init3_4 = Affine(self.params['W2'], self.params['b2'])
ans_conv_init3_5 = Relu()
ans_conv_init3_6 = Affine(self.params['W3'], self.params['b3'])

#############################################


##########   answer check functions   ##############

def checkConvInit():
    chk_1 = ans_conv_init_1==question_1
    chk_2 = ans_conv_init_2==question_2
    chk_3 = ans_conv_init_3==question_3
    chk_4 = ans_conv_init_4==question_4
    chk_5 = ans_conv_init_5==question_5
    chk_6 = ans_conv_init_6==question_6
    chk_7 = ans_conv_init_7==question_7
    if chk_1 and chk_2 and chk_3 and chk_4 and chk_5 and chk_6 and chk_7 :
        print("Greate !!!")
        print("but conv init is continue.")
        print("Let's fill in your answer as follow.")
        print("")
        print(view_cnn_init_2)
        print("")
        print("And check your answer as follow.")
        print("checkConvInit2()")
    else:
        print("Mmmmm.... your answer is incorrect.")
        print("check the hint as follow.")
        print("")
        print("hint_cnn_init_1")
        print("")
        print("And check your answer as follow.")
        print("checkConvInit()")

def checkConvInit2():
    chk_1 = ans_conv_init2_1==question_1
    chk_2 = ans_conv_init2_2==question_2
    chk_3 = ans_conv_init2_3==question_3
    chk_4 = ans_conv_init2_4==question_4
    chk_5 = ans_conv_init2_5==question_5
    chk_6 = ans_conv_init2_6==question_6
    if chk_1 and chk_2 and chk_3 and chk_4 and chk_5 and chk_6:
        print("Greate !!!")
        print("but conv init is continue.")
        print("Let's fill in your answer as follow.")
        print("")
        print(view_cnn_init_3)
        print("")
        print("And check your answer as follow.")
        print("checkConvInit3()")
    else:
        print("Ooops ,, your answer is incorrect.")
        print("Check the hint as follow")
        print("")
        print("hint_cnn_init_2")
        print("")
        print("And check your answer as follow.")
        print("checkConvInit2()")


def checkConvInit3():
    chk_1 = ans_conv_init3_1==question_1
    chk_2 = ans_conv_init3_2==question_2
    chk_3 = ans_conv_init3_3==question_3
    chk_4 = ans_conv_init3_4==question_4
    chk_5 = ans_conv_init3_5==question_5
    chk_6 = ans_conv_init3_6==question_6
    if chk_1 and chk_2 and chk_3 and chk_4 and chk_5 and chk_6:
        print("Greate !!!")
        print("Conv net is defined.")
        print("Next is predict.")
        print("Let's define the predict function as follow.")
        print("")
        print("SimpleConvNet.predict = yourAnswer")
        print("")
        print("And check your answer as follow.")
        print("checkConvPredict()")
    else:
        print("Ooops ,, your answer is incorrect.")
        print("Check the hint as follow")
        print("")
        print("hint_cnn_init_3")
        print("")
        print("And check your answer as follow.")
        print("checkConvInit3()")

def checkConvPredict():
    chk_1 = AnsSimpleConvNet.predict==SimpleConvNet.predict
    if chk_1:
        print("That's good!!")
        print("Next is loss.")
        print("So, define the loss function as follow.")
        print("")
        print("SimpleConvNet.predict = yourAnswer")
        print("")
        print("And check your answer as follow.")
        print("checkConvLoss()")
    else:
        print("Mmmmm... your function is incorrect.")
        print("Check hint as follow.")
        print("")
        print("hint_cnn_predict")
        print("")
        print("And check your answer as follow")
        print("checkConvPredict()")

def checkConvLoss():
    chk_1 = AnsSimpleConvNet.loss==SimpleConvNet.loss
    if chk_1 :
        print("Greate!!!")
        print("Next is accuracy.")
        print("Define the accuracy function and insert as follow.")
        print("")
        print("SimpleConvNet.predict = yourAnswer")
        print("")
        print("And check your answer as follow.")
        print("checkConvLoss()")
        print("")
        print("")
    else:
        print("Ooops your answer is incorrect.")
        print("Check the hint as follow")
        print("")
        print("hint_cnn_loss")
        print("")
        print("And check your answer as follow.")
        print("checkConvLoss()")



#############################################


##########   next chapter function   ##############
def nextChapter(file_name="ch08.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

