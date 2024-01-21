import pandas as pd
import random
import numpy as np
import Levenshtein 
import time

df = pd.read_csv('db/names.csv')

def recommend_names(gender, race, start_letter=None, num_recommendations=10000, similar_to=None, similarity_threshold=5):
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
