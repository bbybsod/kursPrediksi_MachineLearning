# 💸 Kurs Prediksi ML — Prediksi Kurs USD ke IDR (5 Tahun ke Depan)

📈 Proyek machine learning berbasis time series forecasting untuk memprediksi nilai tukar **USD ke IDR selama 5 tahun ke depan** menggunakan model **LSTM (Long Short-Term Memory)**.

## 🧠 Teknologi yang Digunakan

- 📊 **Pandas**, **NumPy** — manipulasi data
- 🧼 **Scikit-learn** — preprocessing (normalisasi, split)
- 🧠 **TensorFlow (Keras)** — model LSTM untuk prediksi
- 📉 **Matplotlib**, **Seaborn** — visualisasi hasil
- 🧪 **Jupyter Notebook** — eksplorasi data dan eksperimen
- 🗂️ Struktur modular `.py` — untuk pipeline produksi

```

## 📁 Struktur Proyek

kurs-prediksi-ml/
├── data/
│ └── kurs_usd_idr.csv # Data historis kurs USD/IDR
├── models/
│ └── lstm_model.py # Definisi arsitektur model
├── preprocessing/
│ └── prepare_data.py # Preprocessing & windowing
├── training/
│ └── train_model.py # Training & saving model
├── forecasting/
│ └── forecast.py # Prediksi ke masa depan
├── notebooks/
│ └── kurs_prediksi_lstm.ipynb # Notebook eksperimen
├── main.py # Script utama (pipeline end-to-end)
├── requirements.txt
└── README.md

```
