import click
import json
from ZScoreScaler import ZScoreScaler

def load_model(model_path):
    with open(model_path, 'r') as file:
        model = json.load(file)
    return model

def predict_price(model : dict, km : int) -> int:
    return int(model['theta0'] + (model['theta1'] * km))




@click.command()
@click.option('--model', type=str, default='thetas.json')
@click.option('--scaler', type=str, default='mileage_scaler.json')
@click.option('--km', type=int)
def predict_price_cli(model, scaler, km):
    try:
        model_path = model
        model = load_model(model_path)
        scaler_path = 'mileage_scaler.json'
        scaler = ZScoreScaler()
        scaler.load_scaler(scaler_path)
        km = scaler.standardize_input(km)
        print(f'Predicted price: {predict_price(model, km)}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    predict_price_cli()

#How to use
# python3 estimate_price.py --model thetas.json --scaler mileage_scaler.json --km=10000
