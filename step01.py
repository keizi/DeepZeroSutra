import numpy as np

# 変数クラス


class Variable:
    def __init__(self, data):
        self.data = data

hub
# インスタンスして代入
data = np.array(1.0)
x = Variable(data)
print(x.data)

# データの上書き
x.data = np.array(2.0)
print(x.data)
