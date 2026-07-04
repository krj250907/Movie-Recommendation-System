# 🎬 Movie Recommendation System

A Machine Learning project that recommends similar movies using **Content-Based Filtering**, **TF-IDF Vectorization**, and **Cosine Similarity**.

---

## 📌 Project Overview

This project recommends movies based on their genres. It uses Natural Language Processing (NLP) techniques to convert movie genres into numerical vectors and finds similar movies using Cosine Similarity.

For example:

**Input**

```
Toy Story
```

**Output**

```
Toy Story (1995)
Toy Story 2 (1999)
Antz (1998)
Monsters, Inc. (2001)
Finding Nemo (2003)
```

---

## 🚀 Features

- Content-Based Movie Recommendation
- TF-IDF Vectorization
- Cosine Similarity Calculation
- Fast Recommendation Generation
- Command-Line Interface
- Lightweight and Easy to Use

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── dataset/
│   └── movies.csv
│
├── models/
│   └── .gitkeep
│
├── src/
│   ├── train.py
│   └── recommend.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/krj250907/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create Virtual Environment

macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run

```bash
python src/train.py
```

Output

```
Movie Recommendation Model Saved Successfully!
```

---

## 🎯 Run the Recommendation System

```bash
python src/recommend.py
```

Example

```
Enter Movie Name:

Toy Story

Recommended Movies:

Toy Story (1995)
Toy Story 2 (1999)
Antz (1998)
Monsters, Inc. (2001)
Finding Nemo (2003)
```

---

## 🧠 How It Works

### Step 1

Load the movie dataset.

### Step 2

Extract movie genres.

### Step 3

Convert genres into TF-IDF vectors.

### Step 4

Calculate Cosine Similarity between all movies.

### Step 5

Store the trained recommendation model.

### Step 6

Recommend Top-N similar movies based on user input.

---

## 📊 Machine Learning Concepts Used

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Feature Engineering
- Text Vectorization
- Model Serialization using Joblib

---

## 📸 Sample Output

```
Enter Movie Name:

Toy Story

Recommended Movies:

Toy Story (1995)
Toy Story 2 (1999)
Antz (1998)
Monsters, Inc. (2001)
Finding Nemo (2003)
```

---

## 📈 Future Improvements

- Movie Posters
- Streamlit Web App
- Flask API
- TMDB API Integration
- IMDb Ratings
- Genre Filters
- User Authentication
- Hybrid Recommendation System

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kartik Raj**

- GitHub: https://github.com/krj250907

If you found this project useful, consider giving it a ⭐ on GitHub.