# 🧠 Flask Emotion Detection

<p align="center">
  <strong>NLP Emotion Analysis • Flask • IBM Watson NLP</strong>
</p> 
<p align="center">
  <strong>Detect emotions from text and identify the dominant emotional state using NLP.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/NLP-Emotion%20Detection-6A1B9A?style=for-the-badge" alt="NLP">
  <img src="https://img.shields.io/badge/IBM-Watson%20NLP-052FAD?style=for-the-badge&logo=ibm&logoColor=white" alt="IBM Watson NLP">
</p>

---

## 📌 Overview

**Flask Emotion Detection** is a Python-based web application that analyzes text and identifies its emotional characteristics using NLP.

The application detects five emotions:

**Anger · Disgust · Fear · Joy · Sadness**

It also determines the **dominant emotion** based on the highest detected score.

---

## ✨ Features

* 🧠 Emotion detection from text
* 📊 Confidence scores for each emotion
* 🎯 Dominant emotion identification
* 🌐 Flask-based web application
* 🔌 REST API endpoint
* ⚠️ Invalid input handling
* 🧪 Unit testing

---

## 🔄 How It Works

```text
        User Input
            │
            ▼
     ┌──────────────┐
     │ Flask Server  │
     └──────┬───────┘
            │
            ▼
     ┌──────────────┐
     │ Emotion      │
     │ Detection    │
     └──────┬───────┘
            │
            ▼
 ┌───────────────────────┐
 │ Anger                 │
 │ Disgust               │
 │ Fear                  │
 │ Joy                   │
 │ Sadness               │
 └───────────┬───────────┘
             │
             ▼
     Dominant Emotion
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                 |
| ----------------- | ----------------------- |
| 🐍 Python         | Application development |
| 🌐 Flask          | Web server and API      |
| 🧠 IBM Watson NLP | Emotion analysis        |
| 🧪 unittest       | Testing                 |

---

## 📁 Project Structure

```text
Flask-Emotion-Detection/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── server.py
├── test_emotion_detection.py
├── requirements/
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/1xcodes-Swapnil/Flask-Emotion-Detection.git
cd Flask-Emotion-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python server.py
```

Open:

```text
http://localhost:5000
```

---

## 🔌 API

### Emotion Detection

```http
GET /emotionDetector
```

### Example

```text
http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20very%20happy%20today
```

The application returns emotion scores along with the detected dominant emotion.

Example:

```json
{
  "anger": 0.01,
  "disgust": 0.01,
  "fear": 0.01,
  "joy": 0.95,
  "sadness": 0.02,
  "dominant_emotion": "joy"
}
```

---

## 🧪 Testing

Run the test suite with:

```bash
python -m unittest test_emotion_detection.py
```

---

## 👤 Author

**Swapnil Mukherjee**

[GitHub](https://github.com/1xcodes-Swapnil)
