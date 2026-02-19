
import torch.nn as nn
import torch
from check_env import device



def model(hidden_parameters=128):
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(3072,hidden_parameters), 
        nn.ReLU(),
        nn.Linear(hidden_parameters,10))
    return model.to(device)

