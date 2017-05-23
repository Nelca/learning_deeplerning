# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from deep_convnet import DeepConvNet
from dataset.mnist import load_mnist
import pdb


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

chk_x = np.array([x_test[0]])
chk_t = t_test[0]
pdb.set_trace()

network = DeepConvNet()
network.load_params("deep_convnet_params.pkl")
y = network.predict(chk_x, train_flg=False)
y = np.argmax(y, axis=1)
print("predicted chk_x label")
print(y)
print("correct chk_x label")
print(chk_t)

