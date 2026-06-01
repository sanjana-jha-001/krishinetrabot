# 🌿 Krishi Neta — AI Crop Disease Detection System

> An end-to-end deep learning web application that detects plant leaf diseases from images in real time. Part of the **Krishi Neta AgriTech AI Platform**.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat-square)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat-square)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🎯 What it does

Upload a photo of a plant leaf → get an instant AI-powered disease prediction with confidence score.

The model is trained on the **PlantVillage dataset** and currently supports:

| Class | Description |
|---|---|
| `Pepper Bell — Healthy` | Healthy pepper bell leaf |
| `Potato — Early Blight` | Alternaria solani fungal infection |
| `Potato — Late Blight` | Phytophthora infestans infection |
| `Potato — Healthy` | Healthy potato leaf |

---

## 🏗️ Architecture

```
User uploads image
       ↓
Flask web server (main.py)
       ↓
PIL preprocessing → resize (256×256) → normalise [0,1]
       ↓
TensorFlow/Keras CNN model (.keras)
       ↓
Softmax → predicted class + confidence %
       ↓
Result rendered in HTML template
```

---

## 🚀 Quick start

**1. Clone the repo**
```bash
git clone https://github.com/sanjana-jha-001/disease.git
cd disease
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python main.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

## 📁 Project structure

```
disease/
├── model_files/
│   └── krishi_neta_disease_predictor1.keras   # Trained CNN model
├── templates/
│   ├── index.html                              # Upload interface
│   └── result.html                            # Prediction result page
├── disease.ipynb                              # Model training notebook
├── main.py                                    # Flask application
└── requirements.txt
```

---

## 🧠 Model details

| Parameter | Value |
|---|---|
| Architecture | Convolutional Neural Network (CNN) |
| Input size | 256 × 256 × 3 |
| Framework | TensorFlow / Keras |
| Dataset | PlantVillage |
| Output | Softmax (4 classes) |

---

## 🛠️ Tech stack

- **Python 3.9+**
- **TensorFlow / Keras** — model training and inference
- **Flask** — web server and REST API
- **Pillow (PIL)** — image preprocessing
- **NumPy** — array operations
- **Werkzeug** — secure file handling

---

## 🌾 Part of the Krishi Neta Platform

This repo is one component of the **Krishi Neta** AgriTech AI ecosystem:

| Component | Repo | Description |
|---|---|---|
| 🌿 Disease Detector | This repo | CNN-based leaf disease classification |
| 🤖 AI Chatbot | [krishinetrabot](https://github.com/sanjana-jha-001/krishinetrabot) | Gemini-powered agricultural assistant |
| 📊 Quality Predictor | [quality_prediction](https://github.com/sanjana-jha-001/quality_prediction) | ML-based produce quality prediction |

---

## 👩‍💻 Author

**Sanjana Jha** — [GitHub](https://github.com/sanjana-jha-001) · [LinkedIn](https://linkedin.com/in/yourprofile)

*Smart India Hackathon 2025 National Winner*

---

## 📄 License

MIT License — feel free to use and build on this project.
