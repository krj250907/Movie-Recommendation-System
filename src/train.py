import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("dataset/movies.csv")

print("First 5 Movies:")
print(movies.head())

# Fill missing genres
movies["genres"] = movies["genres"].fillna("")

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix)

# Save model
joblib.dump((movies, cosine_sim), "models/movie_recommender.pkl")

print("\nMovie Recommendation Model Saved Successfully!")