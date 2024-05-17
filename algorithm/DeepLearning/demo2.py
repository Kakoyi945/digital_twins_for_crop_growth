from torch import nn
import torch
from demo import maize_gru_model

model = maize_gru_model()
model.load_state_dict(torch.load('maize_gru_model.pth'))

print('success')