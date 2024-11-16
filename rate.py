import pandas as pd
import re
import numpy as np

top = pd.read_csv("imdb_top_1000.csv")

print(top[["Poster_Link","Series_Title","Genre","IMDB_Rating"]].head(100))