from name_recommender import recommend_names
import string
import random
import torch
from raw_model import RNN

rnn = torch.load("model/model_2.pth")

from name_generator_v2 import generate_names

def names_generator(gender, category, start_letter=None, quantity=10):
    if start_letter == None:
        start_letter = random.choice(string.ascii_uppercase)
    names = generate_names(rnn, gender=gender, category=category, start_letter=start_letter, temperature=1.0, max_length=15, quantity=quantity)
    return names

def names_recommendor(gender, category, start_letter=None, quantity=10, similarity_threshold=5, similar_to=None):
    names = recommend_names(gender=gender, race=category, start_letter=start_letter, num_recommendations=quantity, similar_to=similar_to, similarity_threshold=similarity_threshold)
    return names
