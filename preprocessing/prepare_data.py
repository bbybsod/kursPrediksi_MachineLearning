import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    return df[['rate']]

def preprocess_data(df, window_size=60):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)
    
    X, y = [], []
    for i in range(window_size, len(scaled)):
        X.append(scaled[i-window_size:i, 0])
        y.append(scaled[i, 0])
    
    X = np.array(X).reshape(-1, window_size, 1)
    y = np.array(y)
    
    return X, y, scaler
