#importing dependencies
import numpy as np
import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#data collection and pre-processing

#loading data from csv file
df = pd.read_csv('Data/movies.csv')
df.head()

#printing the first 5 rows
