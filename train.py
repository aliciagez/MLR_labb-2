import torch
import torch.nn as nn
import torch.optim as optim

model = MyModel()
criterion = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=0.001)

# 2. The Training Loop (The "Practice")
for epoch in range(num_epochs):
    for inputs, targets in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
    print(f"Epoch [{epoch+1}], Loss: {loss.item():.4f}")