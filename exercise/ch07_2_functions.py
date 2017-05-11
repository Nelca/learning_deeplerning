import numpy as np

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
self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                               conv_param['stride'], conv_param['pad'])
self.layers['Relu1'] = Relu()
self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
self.layers['Relu2'] = Relu()
self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

self.last_layer = SoftmaxWithLoss()
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

ans_conv_init_1 = conv_param['filter_num']
ans_conv_init_2 = conv_param['filter_size']
ans_conv_init_3 = conv_param['pad']
ans_conv_init_4 = conv_param['stride']
ans_conv_init_5 = input_dim[1]
ans_conv_init_6 = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
ans_conv_init_7 = int(filter_num * (conv_output_size/2) * (conv_output_size/2))


#############################################


##########   answer check functions   ##############

def checkConvInit():
    chk_1 = 
    if chk_1:
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
    if chk_1:
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
    if chk_1:
        print("Greate !!!")
        print("Conv net is defined.")
        print("")
        print(view_cnn_init_2)
        print("")
        print("And check your answer as follow.")
        print("checkConvInit2()")
    else:
        print("Ooops ,, your answer is incorrect.")
        print("Check the hint as follow")
        print("")
        print("hint_cnn_init_3")
        print("")
        print("And check your answer as follow.")
        print("checkConvInit3()")


#############################################


##########   next chapter function   ##############
def nextChapter(file_name="ch08.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

