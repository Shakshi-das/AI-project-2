#importing libraries
import numpy as np
import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('Data/movies.csv')
df.head()
