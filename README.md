# 🩺 Disease Prediction System

An **ML-powered Disease Prediction System** built with Django that predicts the most likely disease from a set of patient-reported symptoms, using a trained scikit-learn classification model.

Users select symptoms through a searchable checkbox interface, get a predicted disease along with a top-3 confidence breakdown, and every prediction is saved to a history log for later review.

> ⚠️ **Disclaimer:** This project is for educational purposes only and is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

## 📌 Features

- ✅ Predicts across **41 diseases** based on **132 symptoms**
- ✅ Searchable, filterable symptom checklist (no more scrolling through a huge form)
- ✅ Shows **top-3 most likely conditions** with confidence percentages, not just a single guess
- ✅ Server-side **prediction history** stored in the database (SQLite by default)
- ✅ Clean, responsive UI built with plain HTML/CSS/JS — no frontend framework required
- ✅ Trained and benchmarked against **8 different ML algorithms** before selecting the best performer

---

## 🧠 Machine Learning

| Detail | Value |
|---|---|
| Dataset | [Disease Prediction Using Machine Learning](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning) (Kaggle) |
| Symptoms (features) | 132 |
| Diseases (classes) | 41 |
| Training samples | 4,920 |
| Best model | Gradient Boosting Classifier |
| Accuracy (train/test split) | 100% |
| Accuracy (independent holdout set) | **97.6%** |
| Evaluation method | Train/test split + 5-fold cross-validation |

Models compared during development: Gradient Boosting, Random Forest, Extra Trees, Decision Tree, KNN, SVM, Logistic Regression, and Naive Bayes — evaluated on accuracy, precision, recall, and F1-score.

An earlier version of this project used a smaller 10-symptom dataset, which capped accuracy at ~40% due to widespread label ambiguity (multiple diseases sharing identical symptom patterns). Migrating to a richer 132-symptom dataset resolved this and is documented as part of the project's iteration history.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **ML:** scikit-learn, pandas, joblib
- **Database:** SQLite (default Django DB)
- **Frontend:** HTML, CSS, vanilla JavaScript

---

## 📂 Project Structure

```
myproject/
├── manage.py
├── requirements.txt
├── myproject/              # Django project settings
│   ├── settings.py
│   └── urls.py
└── myapp/                  # Main application
    ├── views.py            # Prediction logic + history
    ├── models.py           # PredictionHistory model
    ├── urls.py
    ├── model.pkl            # Trained Gradient Boosting model
    ├── label_encoder.pkl    # Disease label encoder
    ├── symptom_columns.pkl  # Ordered list of 132 symptom names
    └── templates/
        ├── parent.html       # Base template (shared layout/styles)
        ├── index.html        # Home page
        ├── prediction.html   # Symptom selection + prediction form
        └── history.html      # Prediction history log
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/disease-prediction-system.git
cd disease-prediction-system
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply database migrations
```bash
python manage.py migrate
```

### 4. Run the development server
```bash
python manage.py runserver
```

### 5. Open the app
Visit **http://127.0.0.1:8000/** in your browser.

---

## 🖥️ Usage

1. Go to the **Disease Prediction** page.
2. Use the search box to quickly find and check every symptom you're experiencing.
3. Click **Predict** to see the predicted disease and top-3 confidence scores.
4. Visit **Medical History** to review all past predictions, saved automatically to the database.

---

## 📊 Model Training

The full training pipeline — data loading, preprocessing, model comparison, cross-validation, and export of `model.pkl` / `label_encoder.pkl` / `symptom_columns.pkl` — is available in `Disease_Prediction_v2.ipynb`.

To retrain the model:
```bash
jupyter notebook Disease_Prediction_v2.ipynb
```

---

## 🗺️ Roadmap / Possible Improvements

- [ ] Add user authentication so history is tied to individual accounts
- [ ] Add symptom severity/duration as additional features
- [ ] Deploy to a live hosting platform (Render, Railway, etc.)
- [ ] Add unit tests for prediction and history views

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Dataset: [Disease Prediction Using Machine Learning](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning) by kaushil268 on Kaggle
- Built with [Django](https://www.djangoproject.com/) and [scikit-learn](https://scikit-learn.org/)
