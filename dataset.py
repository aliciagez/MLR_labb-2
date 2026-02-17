import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms



transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
                                        
testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)


# add train test split here