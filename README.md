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

Inverse Document Frequency: The IDF of the word is the number of documents in the corpus separated by the frequency of the text.

Therefore the weight of each title is calculated using the term-frequency and inverse document frequency, a word that occurs more times in a title(higher frequency) is more important and words that are present in many titles(like 'The", 'a') are less important due to IDF.

using the TFIDF vectorizer in the sklearn module, we can transform the titles in movies.csv to a collection of vectors of each word and their and weight values.

setting the ngram_range parameters as 1,2 will help us to weigh combinatos of 1 and 2 words. setting analyzer = ‘char_wb’ creates character n-grams only from text inside word boundaries; n-grams at the edges of words are padded with space.

Now that we have transformed the titles to TFIDF vectors, we can implement the search feature by transforming the query to a TFIDF vector and using cosine_similarity to compare the query vector and the list of title vectors and the titles with greater similarity will have higher weights.

Cosine similarity is a mathematical way to measure the similarity between two vectors or sets of information. It's implemented using the sklearn module.
np.argpartition gives us the sorted indices of the 5 highest similarites, which is then used to index into the movies dataframe to get the 5 closest search results.







