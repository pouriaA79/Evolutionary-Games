
import numpy as np


class Activation_Functions():

    def __init__(self):
        pass

    def sigmoid(self, x):

       if  np.all(x >= 0):  # Optimize sigmoid function to avoid extreme data overflow
         return 1.0 / (1 + np.exp(-x))

       else:
             return np.exp(x) / (1 + np.exp(x))
        # return (1 / (1 + np.exp(-x)))

    def relu(self, x):
        return np.heaviside(x, 0) * x

    def tanh(self, x):
        return np.tanh(x)


class NeuralNetwork():

    # Initializing weights and biases
    def __init__(self, layer_sizes):
        self.activation_functions = Activation_Functions()
        self.num_layers = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.biases = []
        self.weights = []
        input_layer_size, hidden_layer_size, output_layer_size = layer_sizes
        self.W1 = np.random.normal(loc=0, scale=1, size=(hidden_layer_size, input_layer_size))
        self.weights.append(self.W1)
        self.W2 = np.random.normal(loc=0, scale=1, size=(output_layer_size, hidden_layer_size))
        self.weights.append(self.W2)
        self.B1 = np.zeros((hidden_layer_size, 1))
        self.B2 = np.zeros((output_layer_size, 1))
        self.biases.append(self.B1)
        self.biases.append(self.B2)

    # Calculating activated values using an activation function (default is sigmoid)
    def activation(self, x):
        return self.activation_functions.tanh(x)

    # Calculating forward propagation to obtain neural network output values.
    def forward(self, x):
        y = x

        for index_layer in range(self.num_layers - 1):
            y = np.matmul(self.weights[index_layer],
                       y) + self.biases[index_layer]
            y = self.activation(y)

        return y

