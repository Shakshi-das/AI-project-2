#source code
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
selected_features = ['genres','keywords','runtime','cast','director']
print(selected_features)

#replacing null values with null string
for feauture in selected_features:
  movies_data[features] = movies_data[features].fillna('')

#combining all the 5 selected features
combined_features= movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['runtime']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_features)

#converting text data to feature vectors
 vectorizer = TfidVectorizer()

feature_vectors = vectorizer-fir_transform(combined_features)
print(feature_vectors)

#cosine similarity

#getting the similarity score using cosine similarity
similarity = cosine_similarity(feature_vectors)
print(similarity)

#getting the movie name from user
movie_name= input("Enter your favourite movie name:")

#creating a list with all the movies names given in the dataset
list_of_all_titles= movies_data['title'].tolist()
print(list_of_all_titles)

#finding the close match for the movie name given by the user
find_close_match= difflib.get_close_matches(movie_name, list_of_all_tiltes)
print(find_close_match)

close_match= find_close_match[0]
print(close_match)

 #finding the index of the movie with title
index_of_the_movie= movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

#getting a list of similar movies
similarity_score= list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

#sorting based on similarity score
sorted_similar_movies= sorted(similarity_score, key= lambda x:x[1], reverse= True)
print(sorted_similar_movies)

#print the name of similar movies based on index
print("Movies suggested for you \n")
