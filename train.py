import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import TitleScreenDataset, transform
from model import SimpleCNN

# Set device to GPU if available, otherwise CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the model, loss function, and optimizer
model = SimpleCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Create the dataset and dataloader for batching
train_dataset = TitleScreenDataset(root_dir='frames/train', transform=transform)
train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Number of epochs to train the model
num_epochs = 3
for epoch in range(num_epochs):
    model.train()  # Set model to training mode
    for images, labels, file_names in train_dataloader:
        images, labels = images.to(device), labels.to(device)  # Move data to the appropriate device
        optimizer.zero_grad()  # Clear gradients
        outputs = model(images)  # Forward pass
        loss = criterion(outputs, labels)  # Compute loss
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')  # Print loss for the epoch

# Save the trained model
torch.save(model.state_dict(), 'titlescreen_model.pth')
