from lore_names.name_recommender import recommend_names
import string
import random
import torch
import torch.nn as nn
import torch.nn.functional as F

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size

        self.i2h = nn.Linear(n_genders + n_categories + input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(n_genders + n_categories + input_size + hidden_size, output_size)
        self.o2o = nn.Linear(hidden_size + output_size, output_size)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, gender, category, input, hidden, temperature=0.9):
        input_combined = torch.cat((gender, category, input, hidden), 1)
        hidden = self.i2h(input_combined)
        output = self.i2o(input_combined)
        output_combined = torch.cat((hidden, output), 1)
        output = self.o2o(output_combined)
        output = self.dropout(output)
        # output = self.softmax(output)
        output = F.log_softmax(output/temperature, dim=1)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

rnn = torch.load("name_generator/model/model_2.pth")

from name_generator.name_generator_v2 import generate_names

def names_generator(gender, category, start_letter=None, quantity=10):
    if start_letter == None:
        start_letter = random.choice(string.ascii_uppercase)
    names = generate_names(rnn, gender=gender, category=category, start_letter=start_letter, temperature=1.0, max_length=15, quantity=quantity)
    return names

def names_recommendor(gender, category, start_letter=None, quantity=10, similarity_threshold=5, similar_to=None):
    names = recommend_names(gender=gender, race=category, start_letter=start_letter, num_recommendations=quantity, similar_to=similar_to, similarity_threshold=similarity_threshold)
    return names

# print(names_generator('male', 'Nord', start_letter="S"))

# print(names_recommendor('male', 'Nord', start_letter="S", similar_to="Odin"))