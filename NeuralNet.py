import numpy as np

class NeuralNet:
    def __init__ (self, x, y):
        self.input=x
        self.weights1= np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2)) 



def sigmoid(x):    
    return 1/(1+np.exp(-x))

