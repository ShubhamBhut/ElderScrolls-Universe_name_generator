import time
start_time = time.time()
from lore_names.name_recommender import recommend_names
import torch
end_time = time.time()

from main import RNN
rnn = RNN()
print(rnn)
print(end_time-start_time)