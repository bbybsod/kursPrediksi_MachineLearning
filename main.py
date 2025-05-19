from preprocessing.prepare_data import load_data, preprocess_data
from training.train import train_model
from forecasting.predict_future import forecast_future
from utils.plot import plot_predictions

if __name__ == "__main__":
    df = load_data('data/kurs_usd_idr.csv')
    X, y, scaler = preprocess_data(df)

    split = int(len(X) * 0.8)
    X_train, y_train = X[:split], y[:split]
    X_val, y_val = X[split:], y[split:]

    model = train_model(X_train, y_train, X_val, y_val, input_shape=(X.shape[1], 1))
    
    last_seq = X[-1].reshape(X.shape[1], 1)
    pred = forecast_future(model, last_seq, steps=1825, scaler=scaler)
    
    plot_predictions(df, pred, df.index[-1] + pd.Timedelta(days=1))
