import pandas as pd
import random

df = pd.read_csv('db/names.csv')

def recommend_names(gender, race, start_letter=None, num_recommendations=10000):
    np_array = df.to_numpy()
    filtered_array = np_array[(np_array[:, 3] == gender) & (np_array[:, 2] == race)]

    if start_letter:
        filtered_array = filtered_array[[name.startswith(start_letter) for name in filtered_array[:, 0]]]

    if len(filtered_array) <= num_recommendations:
        recommended_names = filtered_array[:, 0]
    else:
        recommended_names = random.sample(filtered_array[:, 0].tolist(), num_recommendations)

    return recommended_names

names = recommend_names('male', 'Breton', 'S', 10)
print(names)

