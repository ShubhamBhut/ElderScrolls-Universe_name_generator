import time
start_time = time.time()
import torch
end_time = time.time()
from eso_names.raw_model import RNN
from eso_names.main import names_recommendor, names_generator

print(end_time-start_time)
print(names_recommendor(gender="male", category="Nord", start_letter="S", similar_to="Ragnar", similarity_threshold=5, quantity=5))
print(names_generator(gender="male", category="Argonian", start_letter="A", quantity=5))