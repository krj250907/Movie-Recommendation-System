import joblib

movies, cosine_sim = joblib.load("models/movie_recommender.pkl")

def recommend(movie_name):

    movie_name = movie_name.lower()

    matching_movies = movies[movies["title"].str.lower().str.contains(movie_name)]

    if matching_movies.empty:
        print("\nMovie not found!")
        return

    idx = matching_movies.index[0]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop 10 Recommended Movies\n")

    for i in similarity_scores[1:11]:
        print(movies.iloc[i[0]]["title"])

print("="*45)
print(" Movie Recommendation System ")
print("="*45)

movie = input("\nEnter Movie Name : ")

recommend(movie)