# 🚗 Vehicle AI Assistant

This project is an AI-based assistant that can answer questions related to **cars and bikes**.

Currently, the system is focused on **cars dataset**, and support for **bikes will be added soon**.

---

## 🧠 What this project does

* Takes user questions as input
* Understands the meaning of the question
* Searches the dataset for relevant information
* Returns the most suitable answer

---

## ⚙️ How it works

* The dataset (cars) is converted into meaningful sentences
* A BERT-based embedding model is used to understand text
* The user question is compared with dataset
* The most relevant answer is returned

---

## 🛠️ Technologies Used

* Python
* Sentence Transformers (BERT-based model)
* Pandas
* NumPy

---

## 📂 Project Structure

```
vehicle-ai-assistant/
│
├── app.py
├── data/
│   └── cars.csv
│
├── models/
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

---

## 📌 Example Questions

* Which car has best mileage?
* Car with high horsepower?
* Which car is lightweight?

---

## 🚀 Future Improvements

* Add bike dataset
* Convert into a Streamlit web app
* Improve AI responses using advanced models
* Add better UI and user experience

---

## 💡 Note

This project is currently under development and will be improved step by step.
