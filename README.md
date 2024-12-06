# Movie Recommendation Engine
### Video Demo:  https://youtu.be/Podpd687mEw
### Description: Movie Recommendation engine

This movie recommendation website is an interactive website built using Flask, Python, and JavaScript, with data processing powered by Pandas and scikit-learn. The website's goal is to allow users to search for movies, receive recommendations, and explore curated lists. By combining back-end data processing with a responsive front-end, the platform provides a seamless user experience.

Initially the movie engine was implemented in Jupyter Notebook to test the algorithm, then it was converted to a normal python file. While implementing in jupyter notebook, working with widgets was the method chosen to make the notebook interactive.

The front-end of the website is implemented using HTML,CSS and bootstrap.

The datasets used in this project are linked here:
https://files.grouplens.org/datasets/movielens/ml-25m.zip - only movies.csv and ratings.csv are used from this dataset for the recommendation algorithm.

https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows - this dataset was used for the top 1000 movies list and the suggest feature.

only the top 1000 dataset has links for posters, this is why posters are absent in the recommendation feature.

Recommendation engine: movie_engine.py
The movie engine uses a Collaborative Filtering algorithm to make a list of recommendations.

What is collaborative Filtering?
Collaborative filtering is an information retrieval method that recommends items to users based on how other users with similar preferences and behaviour have interacted with that item.

The movie recommendation engine first implements a search engine, which is used to identify the movie from the dataset based on the users input.

Search Engine:
The search function in movie engine initially takes an input from the user and cleans the title using the clean title function, which removes anything other than the alphanumeric characters from the title using the regular expressions module.

The same clean title function is applied to all the titles in the movies dataset, so that the searched title and the dataset will have similar values.

Term Frequency - Inverse Document Frequency Vectorizer from the science toolkit module is the main operation behind the search engine.

TfIdf is used to identify how important a particular word is in a text.

Term Frequency: In document d, the frequency represents the number of instances of a given word t.

Document Frequency: The occurrence of the word t in the documents,i.e, the number of documents in which the word is present.

Inverse Document Frequency: The IDF of the word is the number of documents in the corpus separated by the frequency of the text.

Therefore the weight of each title is calculated using the term-frequency and inverse document frequency, a word that occurs more times in a title(higher frequency) is more important and words that are present in many titles(like 'The", 'a') are less important due to IDF.

using the TFIDF vectorizer in the sklearn module, we can transform the titles in movies.csv to a collection of vectors of each word and their and weight values.

setting the ngram_range parameters as 1,2 will help us to weigh combinations of 1 and 2 words. setting analyzer = ‘char_wb’ creates character n-grams only from text inside word boundaries; n-grams at the edges of words are padded with space.

Now that we have transformed the titles to TFIDF vectors, we can implement the search feature by transforming the query to a TFIDF vector and using cosine_similarity to compare the query vector and the list of title vectors and the titles with greater similarity will have higher weights.

Cosine similarity is a mathematical way to measure the similarity between two vectors or sets of information. It's implemented using the sklearn module. np.argpartition gives us the sorted indices of the 5 highest similarities, which is then used to index into the movies dataframe to get the 5 closest search results.

Javascript for real-time result fetching
When something is typed on the search box in the index page, the onkeyup() event detects it and calls the search_movie() function implemented in javascript.

the function sends an AJAX request (using fetch) to the /search route, passing the search query.

It receives a list of matching movies from the server and dynamically updates the search results in the HTML.

Recommendation Algorithm:
The recommendation algorithm uses a collaborative filtering algorithm using Pandas to suggest movies.

The algorithm begins by finding similar_users from the ratings dataset that have given the movie being queried a rating greater than 4. Then similar_user_recs is found out by finding the movieIds of all the movies rated above 4 by the similar_users.

similar_user_recs is the filtered to obtain those movies that at least 10 percent of the similar users have liked.

then we calculate the percentage of general users who gave each movie a high rating in order to normalize the recommendations by accounting for overall popularity and avoid over fitting to the preferences of the "similar users".

The percentages from "similar users" (similar_user_recs) and "general users" (all_user_recs) are then combined to calculate a "score" for each movie by dividing the "similar" percentage by the "all" percentage. A higher score indicates that the movie is relatively more popular among similar users compared to the general population.

This prioritizes movies that are highly rated by similar users but not necessarily universally popular, enhancing personalization.

the score is then sorted and the top 11 movies are returned, the top movie will always be the movie searched, so it is excluded and the rest 10 are the final recommended movies by the engine.

Flask application: back-end
At the heart of the platform is the Flask application, which handles routing, user requests, and integration with the recommendation engine. The Flask app includes several routes:

Index Route (/):
Serves the homepage, allowing users to navigate to search, recommendations, or curated movie lists.

Search Route (/search):
Handles movie search queries submitted by users.

When a search term is entered, the route fetches data from the recommendation engine using the search() function.

Results are returned as a JSON object containing a list of matching movies with their IDs and titles.

Recommendation Route (/recommend):
Allows users to request recommendations for a specific movie by providing its ID.

The route interacts with the find_similar_movies() function in the recommendation engine to fetch the ten most similar movies.

Recommendations are displayed, including titles and genres.

Top Movies Route (/top):
Displays a curated list of the top 100 IMDb movies using the top_hundred() function.

Users can view key details such as movie posters, titles, genres, and IMDb ratings.

Random Suggestions Route (/suggest):
Offers a random selection of ten movies from the IMDb dataset.

This feature is powered by the suggest() function, which ensures that each visit delivers a fresh set of movies.









