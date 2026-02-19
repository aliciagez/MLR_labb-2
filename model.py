
import torch.nn as nn
import torch
from check_env import device


hidden_paramaters = 128


def model(hidden_parameters):
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(3072,hidden_paramaters), 
        nn.ReLU(),
        nn.Linear(hidden_paramaters,10)).to(device)
    return model 

my_model = model(hidden_paramaters)