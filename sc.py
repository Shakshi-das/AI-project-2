#importing dependencies
import numpy as np
import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#data collection and pre-processing

#loading data from csv file to apandas dataframe
df = pd.read_csv('Data/movies.csv')

#printing the first 5 rows of the dataframe
df.head()

#number of rows and columns in dataframe
movies_data.shape

#selecting relevant features for recommendations

pd.set_option('display.max_rows', 500)
pd.options.display.max_columns = None
