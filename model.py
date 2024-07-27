import torch
import torch.nn as nn
import torch.nn.functional as F

# Define a simple Convolutional Neural Network (CNN)
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, 1)  # First convolutional layer
        self.conv2 = nn.Conv2d(32, 64, 3, 1)  # Second convolutional layer
        self.fc1 = nn.Linear(64*62*62, 128)  # First fully connected layer
        self.fc2 = nn.Linear(128, 2)  # Output layer (2 classes: with or without titlescreen)

    def forward(self, x):
        x = F.relu(self.conv1(x))  # Apply ReLU activation after the first conv layer
        x = F.relu(self.conv2(x))  # Apply ReLU activation after the second conv layer
        x = F.max_pool2d(x, 2)  # Apply max pooling
        x = torch.flatten(x, 1)  # Flatten the tensor
        x = F.relu(self.fc1(x))  # Apply ReLU activation after the first fully connected layer
        x = self.fc2(x)  # Output layer
        return x

