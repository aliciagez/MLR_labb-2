import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import random
import numpy as np
from model import model
from train import traning_parametser, traning_loop
from check_env import device
from dataset import trainset, testset
from evaluations import base_acc
from evaluations import accuracy_per_class
from evaluations import printing


hidden = model(256)

optimizer, criterion = traning_parametser(hidden, lr=0.0001)

train_loader_3 = DataLoader(trainset, batch_size=32, shuffle=True)
test_loader_3 = DataLoader(testset, batch_size=32, shuffle=True)

traning_loop(hidden, train_loader_3, optimizer, criterion, epochs=30, device=device)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

hidden = model(256)
ex_1 = hidden.load_state_dict(torch.load('./experimetns_models/cifar_3.pth'))
hidden.to(device)
test_loader_1 = DataLoader(testset, batch_size=32, shuffle=True)

base_acc(hidden, test_loader_3, device)

correct_pred, total_pred = accuracy_per_class(test_loader_3, hidden, classes, device) 
printing(total_pred, correct_pred)