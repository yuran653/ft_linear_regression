import pandas as pd
from ZScoreScaler import ZScoreScaler
from MySimpleLinearRegression import MySimpleLinearRegression

def open_dataset(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"An error occurred: open_dataset: {e}")
        return None
    return df

def z_scale_feature(scaler_path: str, feature : pd.Series) -> pd.Series:
    try:
        scaler = ZScoreScaler()
        scaler.fit(feature)
        scaler.save_scaler(scaler_path)
        feature = scaler.standardize(feature)
    except ValueError as e:
        print(f'Error: {e}')
    return feature

def learn_save_model(model_path: str, df: pd.DataFrame, lr=0.01, n_iters=1000):
    lr = MySimpleLinearRegression(lr=lr, n_iters=n_iters)
    lr.train(df)
    lr.save_model(model_path)

csv_path = 'data.csv'
scaler_path = 'mileage_scaler.json'
model_path = 'thetas.json'

df = open_dataset(csv_path)

df['km'] = z_scale_feature(scaler_path, df['km'])

learn_save_model(model_path, df, )
