import pandas as pd
import random
import numpy as np
import Levenshtein 
import time

df = pd.read_csv('db/names.csv')

def recommend_names(gender, race, start_letter=None, num_recommendations=10000, similar_to=None, similarity_threshold=3):
    np_array = df.to_numpy()
    filtered_array = np_array[(np_array[:, 3] == gender) & (np_array[:, 2] == race)]

    if start_letter:
        filtered_array = filtered_array[[name.startswith(start_letter) for name in filtered_array[:, 0]]]

    if similar_to:
        filtered_array[:, 0] = filtered_array[:, 0].astype(str)
        distances = np.array([Levenshtein.distance(similar_to, name) for name in filtered_array[:, 0]])
        
        filtered_array = filtered_array[distances <= similarity_threshold]

    if len(filtered_array) <= num_recommendations:
        recommended_names = filtered_array[:, 0]
    else:
        recommended_names = random.sample(filtered_array[:, 0].tolist(), num_recommendations)

    return recommended_names

input_gender = 'male'
input_race = 'Breton'
input_start_letter = 'S'
input_similar_to = 'Savogoth'

start_time = time.time()
names = recommend_names(input_gender, input_race, start_letter=input_start_letter, num_recommendations=10, similar_to=input_similar_to, similarity_threshold=5)
end_time = time.time()
print(names)
print(end_time - start_time)

