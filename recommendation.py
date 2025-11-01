import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

movies['genre'] = movies['genre'].str.split('|')


mlb = MultiLabelBinarizer()
genre_features = mlb.fit_transform(movies['genre'])


similarity = cosine_similarity(genre_features)

def recommend_movies(movie_name, n=5):

    if movie_name not in movies['movie_name'].values:
        return f"Sorry, '{movie_name}' not found in the dataset."

    idx = movies[movies['movie_name'] == movie_name].index[0]

    sim_scores = list(enumerate(similarity[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:n+1]

    movie_indices = [i[0] for i in sim_scores]

    return movies['movie_name'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    movie_to_test = "Inception"  # Change this to any movie in your CSV
    recommended = recommend_movies(movie_to_test, n=5)
    
    print(f"Movies similar to '{movie_to_test}':")
    if isinstance(recommended, list):
        for m in recommended:
            print(m)
    else:
        print(recommended)

