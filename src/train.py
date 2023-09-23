from data_preparation import load_data, preprocess_data
from model import train_model

if __name__ == "__main__":
    data = load_data('../data/housing_data2.csv')
    preprocessed_data = preprocess_data(data)
    
    X = preprocessed_data.drop('price', axis=1)
    y = preprocessed_data['price']

    model = train_model(X, y)

