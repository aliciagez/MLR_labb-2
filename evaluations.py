import torch
import torch.nn as nn
from check_env import device



def base_acc(hidden, testloader, device):
    hidden.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in testloader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = hidden(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total

def accuracy_per_class(testloader, hidden, classes, device):
    hidden.eval()
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}
    with torch.no_grad():
       for images, labels in testloader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = hidden(images)
            _, predictions = torch.max(outputs, 1)
            for label, prediction in zip(labels, predictions):
                   classname = classes[label.item()]
                   total_pred[classname] += 1 
                   if prediction == label:
                        correct_pred[classname] += 1 
    return correct_pred, total_pred
       

def printing(total_pred, correct_pred):  
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')
