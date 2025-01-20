# Z-score scaler

import pandas as pd
import json

class ZScoreScaler:
    def __init__(self, mean=None, std=None):
        self.mean = mean
        self.std = std

    def fit(self, feature: pd.Series):
        self.mean = feature.mean()
        self.std = feature.std()
        if self.std == 0:
            raise ValueError("Standard deviation is zero. Cannot standardize.")

    def standardize(self, feature: pd.Series) -> pd.Series:
        if self.mean is None or self.std is None:
            raise ValueError("Scaler has not been fitted yet.")
        return (feature - self.mean) / self.std

    def save_scaler(self, file_path: str):
        model = {'mean': self.mean, 'std': self.std}
        with open(file_path, 'w') as file:
            json.dump(model, file)

    def load_scaler(self, file_path: str):
        with open(file_path, 'r') as file:
            scales = json.load(file)
        self.mean = scales.get('mean')
        self.std = scales.get('std')

    def standardize_input(self, value: float) -> float:
        if self.mean is None or self.std is None:
            raise ValueError("Scaler has not been fitted yet.")
        return (value - self.mean) / self.std
    