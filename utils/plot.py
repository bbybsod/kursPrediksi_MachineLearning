import matplotlib.pyplot as plt
import pandas as pd

def plot_predictions(real_df, predicted_rates, start_date):
    future_dates = pd.date_range(start_date, periods=len(predicted_rates))
    pred_df = pd.DataFrame(predicted_rates, index=future_dates, columns=['Predicted Rate'])
    
    plt.figure(figsize=(12,6))
    plt.plot(real_df[-365:], label='Real Rate (1yr)')
    plt.plot(pred_df, label='Predicted Rate (Next 5yr)', color='orange')
    plt.title('Prediksi Kurs IDR/USD')
    plt.xlabel('Tanggal')
    plt.ylabel('Kurs')
    plt.legend()
    plt.grid()
    plt.show()
