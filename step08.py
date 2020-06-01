import numpy as np

# 変数クラス


class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None  # 生みの親

    def set_creator(self, func):
        self.creator = func

    def backword(self):
        funcs = [self.creator]

        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backword(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)


# 関数クラス


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator(self)  # 出力変数に生みの親を設定
        self.input = input
        self.output = output
        return output

    def forward(self, x):
        raise NotImplementedError()

    def backword(self, gy):
        raise NotImplementedError()

# 2乗関数


class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y

    def backword(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

# Exp関数


class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backword(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx


# 連結計算
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

y.grad = np.array(1.0)
y.backword()

print(x.grad)
