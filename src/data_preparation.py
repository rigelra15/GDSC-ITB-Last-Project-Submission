import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    preprocessed_data = data.copy()
    return preprocessed_data
