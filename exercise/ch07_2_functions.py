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

view_cnn_init_2 = """
self.params = {}
self.params['W1'] = weight_init_std * \
                np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
self.params['b1'] = np.zeros(filter_num)
self.params['W2'] = weight_init_std * \
                np.random.randn(pool_output_size, hidden_size)
self.params['b2'] = np.zeros(hidden_size)
self.params['W3'] = weight_init_std * \
                np.random.randn(hidden_size, output_size)
self.params['b3'] = np.zeros(output_size)
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

ans_cont_init_1 = conv_param['filter_num']
ans_cont_init_2 = conv_param['filter_size']
ans_cont_init_3 = conv_param['pad']
ans_cont_init_4 = conv_param['stride']
ans_cont_init_5 = input_dim[1]
ans_cont_init_6 = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
ans_cont_init_7 = int(filter_num * (conv_output_size/2) * (conv_output_size/2))


#############################################


##########   answer check functions   ##############

def checkConvInit():
    if chk_1:
        print("")
        print("")
        print("")
        print("")
        print("")


#############################################


##########   next chapter function   ##############
def nextChapter(file_name="ch08.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

