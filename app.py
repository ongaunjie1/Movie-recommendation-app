import streamlit as st
import pickle
import requests

## Load movie data (shows index)
movies = pickle.load(open("movies_list.pkl", 'rb'))
## Load similarity
similarity = pickle.load(open("similarity.pkl", 'rb'))

movies_list = movies['title'].values

st.header("Movie Recommendation App (Cosine Similarity)")   
selected = st.selectbox("Select movie from dropdown", movies_list)
 
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

## Fetch movie poster from themoviedb API
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=880450881b60cf0464769c0b15e3fdac&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path'] 
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path
    
if st.button("Recommend movies"):
    top5_movie, movie_poster = recommend(selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    if top5_movie:
        # Create columns dynamically
        num_columns = len(top5_movie)
        columns = st.columns(num_columns)

    # Display movie titles in columns
    for i in range(num_columns):
        with columns[i]:
            st.text(top5_movie[i])
    
    # Display movie posters
    for i in range(num_columns):
        with columns[i]:
            st.image(movie_poster[i])

            
