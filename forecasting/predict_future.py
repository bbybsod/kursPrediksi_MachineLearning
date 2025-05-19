import numpy as np

def forecast_future(model, last_sequence, steps, scaler):
    current_input = last_sequence.reshape(1, last_sequence.shape[0], 1)
    predictions = []
    
    for _ in range(steps):
        pred = model.predict(current_input)[0, 0]
        predictions.append(pred)
        current_input = np.append(current_input[:, 1:, :], [[[pred]]], axis=1)
    
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
