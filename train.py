import torch
import torch.nn as nn
import torch.optim as optim
from model import model
from check_env import device

def traning_parametser(model, lr):
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    return optimizer, criterion


def traning_loop(model, trainloader,optimizer, criterion, epochs, device):
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for inputs, targets in trainloader:
            inputs = inputs.to(device, non_blocking=True)
            targets = targets.to(device, non_blocking=True)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        print(f"Epoch [{epoch+1}], Loss: {loss.item():.4f}")
    

    