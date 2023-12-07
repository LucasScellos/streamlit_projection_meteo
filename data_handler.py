# data_handler.py
import pandas as pd

def load_data(city):
    # Charger vos données à partir du CSV en fonction de la ville
    # Remplacez cette étape par le chargement de vos propres données
    df = pd.read_csv(f'data/temperature_data.csv')
    data = df[df["Ville"]==city]
    return data
