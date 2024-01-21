import torch
import string
import pandas as pd
import torch.nn.functional as F
import random
import pkg_resources

all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters) + 1 # Plus EOS marker

def load_df():
    stream = pkg_resources.resource_stream(__name__, 'db/names.csv')
    return pd.read_csv(stream)

df = load_df()

all_categories = list(df['race'].unique())
n_categories = len(all_categories)

n_genders = 2
all_genders = ['male', 'female']
def genderTensor(gender):
    li = all_genders.index(gender)
    tensor = torch.zeros(1, n_genders)
    tensor[0][li] = 1
    return tensor

# Random item from a list
def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

# One-hot vector for category
def categoryTensor(category):
    li = all_categories.index(category)
    tensor = torch.zeros(1, n_categories)
    tensor[0][li] = 1
    return tensor

# One-hot matrix of first to last letters (not including EOS) for input
def inputTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li in range(len(line)):
        letter = line[li]
        tensor[li][0][all_letters.find(letter)] = 1
    return tensor

# ``LongTensor`` of second letter to end (EOS) for target
def targetTensor(line):
    letter_indexes = [all_letters.find(line[li]) for li in range(1, len(line))]
    letter_indexes.append(n_letters - 1) # EOS
    return torch.LongTensor(letter_indexes)


def generate_name(rnn, gender, category, start_letter='A', max_length=20, temperature=1.0):
    with torch.no_grad():
        input_tensor = inputTensor(start_letter)
        hidden = rnn.initHidden()
        gender = genderTensor(gender)
        category = categoryTensor(category)

        output_name = start_letter

        for i in range(max_length):
            output, hidden = rnn(gender, category, input_tensor[0], hidden)
            probabilities = F.softmax(output / temperature, dim=1)
            
            # Use probabilistic random sampling to choose the next character
            sampled_index = torch.multinomial(probabilities.squeeze(), 1)
            # print(probabilities.squeeze())
            # print(sampled_index)

            if sampled_index == 58:
                break
            else:
                sampled_char = all_letters[sampled_index.item()]
                output_name += sampled_char
            input_tensor = inputTensor(sampled_char)

        return output_name

def generate_names(rnn, gender, category, start_letter, temperature, max_length=15, quantity=10):
    names = []
    for i in range(quantity):
        name = generate_name(rnn, gender=gender, category=category, start_letter=start_letter, max_length=max_length, temperature=temperature) 
        names.append(name)
    return names

