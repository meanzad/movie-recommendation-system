import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

from flask import Flask,redirect,render_template, request, session

movies = pd.read_csv("movies.csv")

top = pd.read_csv("imdb_top_1000.csv")

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]","",title)

movies["clean_title"] = movies["title"].apply(clean_title)



vectorizer = TfidfVectorizer(ngram_range=(1,2),analyzer="char_wb")

tfidf = vectorizer.fit_transform(movies['clean_title'])



def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec,tfidf).flatten()
    indices = np.argpartition(similarity,-5)[-5:]
    results = movies.iloc[indices][::-1]
    return results

ratings = pd.read_csv("ratings.csv")

def find_similar_movies(movie_id):
    similar_users = ratings[(ratings['movieId'] == movie_id) & (ratings["rating"] > 4)]['userId'].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings['rating'] > 4)]["movieId"]
    
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .10]
   
    all_users = ratings[(ratings['movieId'].isin(similar_user_recs.index)) & (ratings['rating'] > 4)]
    all_user_recs = all_users['movieId'].value_counts() / len(all_users['userId'].unique())

    rec_percentages = pd.concat([similar_user_recs,all_user_recs],axis = 1)
    rec_percentages.columns = ["similar","all"]
    
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    
    rec_percentages = rec_percentages.sort_values("score",ascending = False)
    return rec_percentages.iloc[range(1,11)].merge(movies,on = "movieId")[["score","title","genres"]]


def top_hundred():
    return top[["Poster_Link","Series_Title","Genre","IMDB_Rating"]].head(100)

def suggest():

    ind = random.sample(range(1001), 10)
    ind.sort()
    res = top.iloc[ind]
    return res[["Poster_Link","Series_Title","Genre","IMDB_Rating"]]

    

    

