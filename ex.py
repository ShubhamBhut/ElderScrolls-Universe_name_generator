import time
start_time = time.time()
from lore_names.name_recommender import recommend_names
import torch
end_time = time.time()
from eso_names.raw_model import RNN
from eso_names.main import names_recommendor

print(end_time-start_time)
print(names_recommendor(gender="male", category="Nord"))