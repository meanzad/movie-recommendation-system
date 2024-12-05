# Movie Recommendation Engine
### Video Demo:  https://youtu.be/Podpd687mEw
### Description: Movie Recommendation engine

This movie recommendation website is an interactive website built using Flask, Python, and JavaScript, with data processing powered by Pandas and scikit-learn. The website's goal is to allow users to search for movies, receive recommendations, and explore curated lists. By combining backend data processing with a responsive frontend, the platform provides a seamless user experience.

Initially the movie engine was implemented in Jupyter Notebook to test the algorithm, then it was converted to a normal python file. While implementing in jupyter notebook, working with widgets was the method chosen to make the notebook interactive.

##### The datasets used in this project are linked here:

https://files.grouplens.org/datasets/movielens/ml-25m.zip - only movies.csv and ratings.csv are used from this dataset for the recommendation algorithm.

https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows - this dataset was used for the top 1000 movies list and the suggest feature.

only the tep 1000 dataset has links for posters, this is why posters are absent in the recommendation feature.

#### Recommendation engine: movie_engine.py

The movie engine uses a Collaborative Filtering algorithm to make a list of recommendations.

##### What is collaborative Filtering?

Collaborative filtering is an information retrieval method that recommends items to users based on how other users with similar preferences and behavior have interacted with that item.

The movie recommendation engine first implements a search engine, which is used to identify the movie from the dataset based on the users input.

##### Search Engine:

The search function in movie engine initially takes an input from the user and cleans the title using the clean title function, which removes anything other than the alphanumeric characters from the title using the regular expressions module.

The same clean title function is appled to all the titles in the movies dataset, so that the searched title and the dataset will have similar values.

Term Frequency - Inverse Document Frequency Vectorizer from the science toolkit module is the main operation behind the search engine.

TfIdf is used to identify how important a particular word is in a text.

Term Frequency: In document d, the frequency represents the number of instances of a given word t.

Document Frequency: The occurence of the word t in the documents,i.e, the number of documents in which the word is present.



