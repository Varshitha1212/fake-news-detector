[README.md](https://github.com/user-attachments/files/21690674/README.md)
# 📰 TruePoint – Fake News Detector

TruePoint is a simple and stylish web-based fake news detection app built with Flask. It uses natural language processing (NLP) techniques and a machine learning model to predict whether a given news article is real or fake.

---

## 🚀 Features

- Paste any news article into the text box to analyze.
- Instantly get predictions with confidence percentage.
- Clean, pastel-themed user interface for an enjoyable user experience.
- Easy-to-run locally using Python and Flask.

---

## 🧠 How It Works

The app is trained using a logistic regression model with a TF-IDF vectorizer on a dataset of real and fake news articles. When a user submits news text, the app:

1. Preprocesses and vectorizes the text.
2. Predicts using the trained machine learning model.
3. Returns a classification result with a confidence score.

---

## 📁 Project Structure

```
fake-news-detector/
├── app.py               # Flask application
├── trainmodel.py        # Script to train and save the model
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # TF-IDF vectorizer
└── templates/
    └── index.html       # Web UI template
```

---

## 🛠️ Installation & Running Locally

1. Clone the repository:
```bash
git clone https://github.com/Varshitha1212/fake-news-detector.git
cd fake-news-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open in your browser:
```
http://127.0.0.1:5000/
```

---

## 📦 Requirements

- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- Numpy

(You can add a `requirements.txt` file by running `pip freeze > requirements.txt`)


## ✨ Future Improvements

- Add user feedback options for false predictions.
- Improve model accuracy with a larger dataset.
- Deploy the app to the web (e.g. Render, Hugging Face Spaces).

---

## 🙋‍♀️ Author

Malladi Varshitha  
[GitHub](https://github.com/Varshitha1212)
