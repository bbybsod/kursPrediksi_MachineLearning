💸 Kurs Prediksi ML — Prediksi Kurs USD ke IDR (5 Tahun ke Depan)
📈 Time series forecasting proyek berbasis machine learning dengan model LSTM untuk memprediksi nilai tukar USD ke IDR hingga 5 tahun ke depan berdasarkan data historis.

🧠 Teknologi yang Digunakan
📊 Pandas & NumPy – manipulasi data

📉 Scikit-learn – preprocessing data

🧠 TensorFlow (Keras) – deep learning (LSTM)

📈 Matplotlib – visualisasi hasil

📒 Jupyter Notebook – eksplorasi & eksperimen

🧪 Struktur modular Python – untuk produksi & pengembangan jangka panjang

📁 Struktur Proyek
bash
Copy
Edit
kurs-prediksi-ml/
├── data/
│   └── kurs_usd_idr.csv       # Data kurs historis (format CSV)
├── models/
│   └── lstm_model.py          # Arsitektur model LSTM
├── preprocessing/
│   └── prepare_data.py        # Normalisasi & windowing time series
├── training/
│   └── train_model.py         # Training & saving model
├── forecasting/
│   └── forecast.py            # Prediksi ke masa depan
├── notebooks/
│   └── kurs_prediksi_lstm.ipynb  # Eksperimen interaktif
├── requirements.txt
└── README.md
📦 Instalasi
bash
Copy
Edit
git clone https://github.com/username/kurs-prediksi-ml.git
cd kurs-prediksi-ml
pip install -r requirements.txt
🛠 Cara Pakai
Siapkan data di folder data/kurs_usd_idr.csv

Jalankan notebook:

bash
Copy
Edit
jupyter notebook notebooks/kurs_prediksi_lstm.ipynb
Atau gunakan versi modular .py untuk pipeline end-to-end:

bash
Copy
Edit
python main.py
📈 Format Data CSV
csv
Copy
Edit
date,rate
2015-01-01,12500.00
2015-01-02,12520.00
...
2025-05-19,16462.00
📊 Contoh Output
Prediksi kurs untuk 1825 hari (5 tahun)

Visualisasi hasil prediksi

Model tersimpan untuk penggunaan ulang

🧪 Roadmap Selanjutnya
 Fine-tuning hyperparameter (GridSearch/Optuna)

 Evaluasi model ARIMA vs LSTM vs Prophet

 Deployment ke web (Streamlit/FastAPI)

 Auto retraining saat data baru masuk

🤝 Kontribusi
Pull Request sangat welcome! Feel free untuk fork, edit, dan push 🚀
Buat ide peningkatan? Buka issue atau DM aja langsung!

👑 Credits
Created with ❤️ by @lovhriel
Data dari Bank Indonesia & Investing.com

