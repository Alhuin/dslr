import numpy as np

from dslr.stats import sigmoid_


class LogisticRegression:
    """
    Logistic Regression Class, fitting data and predicting the values
    """

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):  # pylint: disable=missing-function-docstring, invalid-name
        # init parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            # approximate
            y_predicted = self.approximation(X)

            weights_derivative = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            bias_derivative = (1 / n_samples) * np.sum(y_predicted - y)

            # gradient descent
            self.weights -= self.learning_rate * weights_derivative
            self.bias -= self.learning_rate * bias_derivative

    def predict(self, X):  # pylint: disable=invalid-name
        linear_model = np.dot(X, self.weights) + self.bias  # linear_model + sigmoid
        y_predicted = sigmoid_(linear_model)
        return [1 if i > 0.5 else 0 for i in y_predicted]

    def approximation(self, X):  # pylint: disable=invalid-name
        linear_model = np.dot(X, self.weights) + self.bias
        return sigmoid_(linear_model)
