# 💓 CardioCare: Predicting Cardiovascular Disease Risks

CardioCare is a machine learning-based web application built with Streamlit that helps assess an individual's risk of cardiovascular disease (CVD) using clinical and lifestyle data.

---

## 🚀 Features

- 🔍 Real-time CVD risk prediction using Random Forest
- 📊 Dataset preview and exploration
- 📁 Model saving and loading using `joblib`
- 💡 User-friendly interface with interactive sidebar

---

## 🧠 ML Model

The model is trained on the **Cardiovascular Disease dataset** from Kaggle. It uses the following features:

- `age` (in days)
- `gender` (1 = female, 2 = male)
- `height` (in cm)
- `weight` (in kg)
- `ap_hi` (systolic BP)
- `ap_lo` (diastolic BP)
- `cholesterol` (1: normal, 2: above normal, 3: well above normal)
- `gluc` (same as cholesterol)
- `smoke`, `alco`, `active` (1 = yes, 0 = no)
- `cardio` (target: 1 = disease, 0 = healthy)

---

## 🧰 Tech Stack

- `Python 3`
- `Pandas`, `Scikit-learn`
- `Streamlit`
- `joblib`

---

## 🗂️ Folder Structure

CardioCare/
├── cardio_train.csv # Dataset (semicolon-separated)
├── CardioCare.py # Streamlit web app
├── train_model.py # Model training + export
├── cardio_model.pkl # Saved model (via joblib)
└── README.md # Project documentation
