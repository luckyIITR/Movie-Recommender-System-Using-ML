import pickle
import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# ----------------------- Fetch movie details -----------------------
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch movie data.")
        return {
            "title": "N/A",
            "poster": "",
            "rating": "N/A",
            "genres": "N/A",
            "overview": "No details available."
        }

    poster_path = data.get('poster_path')
    poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

    return {
        "title": data.get('title', 'N/A'),
        "poster": poster_url,
        "rating": data.get('vote_average', 'N/A'),
        "genres": ", ".join([g['name'] for g in data.get('genres', [])]),
        "overview": data.get('overview', 'No description.')
    }

# ----------------------- Recommend Movies -----------------------
def recommend(movie_title):
    index = movies[movies['title'] == movie_title].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_details = fetch_movie_details(movie_id)
        recommended_movies.append(movie_details)

    return recommended_movies

# ----------------------- Streamlit UI -----------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #F63366;'>🎥 Movie Recommender System</h1>",
    unsafe_allow_html=True
)

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Search or select a movie", movie_list)

if st.button('🔍 Show Recommendations'):
    with st.spinner("Fetching recommendations..."):
        recommendations = recommend(selected_movie)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>Top 5 Similar Movies</h3>", unsafe_allow_html=True)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(recommendations[idx]["poster"], use_column_width=True)
            st.markdown(f"**{recommendations[idx]['title']}**")
            st.markdown(f"⭐ {recommendations[idx]['rating']}")
            st.markdown(f"🎭 {recommendations[idx]['genres']}")
            st.markdown(f"<p style='font-size: small;'>{recommendations[idx]['overview'][:150]}...</p>", unsafe_allow_html=True)