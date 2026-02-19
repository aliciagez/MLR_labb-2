import torch
import torch.nn as nn
import torch.optim as optim
from model import my_model

optimizer = optim.Adam(my_model.parameters(), lr=0.001)


criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 10
train_losses = []
test_losses = []

def traning_loop(model):
    for epoch in range(epochs):
        model.train()
        for i, data in enumerate(trainloader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
        return epoch+1, loss 
    
    
print(f"Epoch [{epoch+1}], Loss: {loss.item():.4f}")