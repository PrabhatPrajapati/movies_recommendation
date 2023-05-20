# import streamlit as st
import pandas as pd
import joblib
# similarity=joblib.load("similarity.pkl")
# st.title("Movie Recommender System")
# movie=pd.read_csv("tmdb_5000_movies.csv")
# name=movie["title"].values
# option = st.selectbox(
#      'How would you like to be contacted?',
#      name)

# def recommendaction(name):
#     movie_index=movie[movie["title"]==name].index[0]
#     distance=similarity[movie_index]
#     movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda X:X[1])[1:6]
#     recommanded_movie=[]
#     for i in movie_list:
#         recommanded_movie.append(movie.iloc[i[0]].title)
#     return recommanded_movie

# if st.button("Recommend"):
#     recommand=recommendaction(option)
#     for i in recommand:
#         st.write(i)


import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# import streamlit.components.v1 as components

# imageCarouselComponent = components.declare_component("image-carousel-component")


# imageUrls = [
#     fetch_poster(1632),
#     fetch_poster(299536),
#     fetch_poster(17455),
#     fetch_poster(2830),
#     fetch_poster(429422),
#     fetch_poster(9722),
#     fetch_poster(13972),
#     fetch_poster(240),
#     fetch_poster(155),
#     fetch_poster(598),
#     fetch_poster(914),
#     fetch_poster(255709),
#     fetch_poster(572154)
   
#     ]


imageCarouselComponent(imageUrls=st.image[914], height=200)


st.header('Movie Recommender System')
movies = pd.read_csv("file1.csv")
similarity = joblib.load("similarity.pkl")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





