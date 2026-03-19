# 🧠 Fake Job Detection System

## 📌 Project Description

This project is a **Machine Learning-based Fake Job Detection System** that identifies whether a job posting is **real or fraudulent**.

With the increasing number of online job scams, this system helps users detect fake job listings by analyzing textual information such as job title, description, company profile, and requirements.

The model uses **Natural Language Processing (NLP)** techniques along with **TF-IDF vectorization** to convert text into numerical features and then applies a classification algorithm to predict the result.

---

## 🚀 Key Features

* 🔍 Detect fake vs real job postings
* 🧠 NLP-based text analysis
* 📊 TF-IDF feature extraction
* ⚡ Fast prediction using trained model
* 💻 Simple interface to test job data

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* NLP (TF-IDF Vectorizer)
* Pickle (model saving/loading)

---

## 📂 Project Structure

```id="s3k9la"
Fake-Job-Detection/
│── app.py                     # Main application
│── dataset.py                 # Data processing script
│── train_model.py             # Model training script
│── job_model.pkl              # Trained ML model
│── tfidf_vectorizer.pkl       # TF-IDF vectorizer
│── india_fake_job_dataset.csv # Dataset
│── run_app.bat                # Run script (Windows)
│── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Data Preprocessing

* Cleaned dataset (removed null values, unnecessary columns)
* Combined text features (title, description, etc.)
* Converted text into numerical form using **TF-IDF Vectorization**

---

### 2️⃣ Model Training

* Trained classification model on labeled dataset
* Model learns patterns of fake vs real job postings
* Saved using `pickle` for reuse

---

### 3️⃣ Prediction System

* User inputs job details
* Text is transformed using saved TF-IDF vectorizer
* Model predicts:

  * ✅ Real Job
  * ❌ Fake Job

---

## ▶️ How to Run the Project

1. Clone the repository:

```id="q9n2la"
git clone https://github.com/your-username/fake-job-detection.git
```

2. Navigate to folder:

```id="z1k3pm"
cd fake-job-detection
```

3. Install dependencies:

```id="m4t8xr"
pip install -r requirements.txt
```

4. Run the application:

```id="p2v7lk"
python app.py
```

OR (Windows):

```id="x8c1dr"
run_app.bat
```

---

## 📊 Model Information

* Technique: Text Classification
* Feature Extraction: TF-IDF
* Input: Job title, description, etc.
* Output: Fake / Real classification

---

## 📈 Future Improvements

* Use deep learning (LSTM / BERT)
* Improve accuracy with more data
* Deploy as web application
* Add browser extension for job detection

---

## 👨‍💻 Author

**Saksham Rathi**
B.Tech CSE | Data Science Enthusiast

---

## ⭐ Conclusion

This project demonstrates how Machine Learning and NLP can be used to solve real-world problems like detecting fraudulent job postings and improving online job search safety.

---
