# Linear Regression with Gradient Decent and MSE as loss function

import pandas as pd
import numpy as np
import json

class MySimpleLinearRegression:
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.theta0 = 0
        self.theta1 = 0

    def estimate_price(self, km : int):
        return (self.theta0 + (self.theta1 * km))

    def train(self, df : pd.Series):
        m = df['km'].size
        for _ in range(self.n_iters):
            self.theta1 -= (self.lr / m) * np.sum((self.estimate_price(df['km']) - df['price']) * df['km'])
            self.theta0 -= (self.lr / m) * np.sum(self.estimate_price(df['km']) - df['price'])

    def save_model(self, file_path : str):
        model = {
            'theta0': self.theta0,
            'theta1': self.theta1
        }
        with open(file_path, 'w') as file:
            json.dump(model, file)
