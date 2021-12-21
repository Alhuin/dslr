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

    def fit(self, x_train, y_test):  # pylint: disable=missing-function-docstring, invalid-name
        """
        train x data
        :param x_train:    the path containing the dataset as csv
        :param y_test:    the path containing the dataset as csv
        """
        # init parameters
        n_samples, n_features = x_train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            # approximate
            y_predicted = self.approximation(x_train)

            weights_derivative = (1 / n_samples) * np.dot(x_train.T, (y_predicted - y_test))
            bias_derivative = (1 / n_samples) * np.sum(y_predicted - y_test)

            # gradient descent
            self.weights -= self.learning_rate * weights_derivative
            self.bias -= self.learning_rate * bias_derivative

    def predict(self, to_predict):  # pylint: disable=invalid-name
        y_predicted = self.approximation(to_predict)
        return [1 if i > 0.5 else 0 for i in y_predicted]

    def approximation(self, to_approx):  # pylint: disable=invalid-name
        linear_model = np.dot(to_approx, self.weights) + self.bias
        return sigmoid_(linear_model)
