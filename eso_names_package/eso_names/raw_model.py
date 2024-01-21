import torch
import torch.nn as nn
import torch.nn.functional as F
n_genders = 2
n_categories = 10

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
