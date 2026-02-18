
import torch.nn as nn
import torch
from check_env import device

amout_data = 3072
in_put_paramaters = 128
out_put_paramaters = 128
amount_of_classes = 10


model = nn.Sequential(nn.flatten(),nn.Linear(amout_data, in_put_paramaters), nn.ReLU(), nn.Linear(amount_of_classes)).to(device)
