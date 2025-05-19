from tensorflow.keras.callbacks import EarlyStopping
from models.lstm_model import build_lstm_model

def train_model(X_train, y_train, X_val, y_val, input_shape):
    model = build_lstm_model(input_shape)
    model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=50,
        batch_size=32,
        callbacks=[EarlyStopping(patience=5, restore_best_weights=True)],
        verbose=1
    )
    return model
