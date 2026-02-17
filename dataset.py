import torch
from torchvision import datasets, transforms
import sys
print(sys.executable)



transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
                                        
testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)


