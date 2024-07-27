import torch
from torch.utils.data import DataLoader
from dataset import TitleScreenDataset, transform
from model import SimpleCNN

# Set device to GPU if available, otherwise CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the model and load the trained parameters
model = SimpleCNN().to(device)
model.load_state_dict(torch.load('titlescreen_model.pth'))
model.eval()  # Set model to evaluation mode

# Load your validation set similar to the training set
val_dataset = TitleScreenDataset(root_dir='frames/val', transform=transform)
val_dataloader = DataLoader(val_dataset, batch_size=32, shuffle=False)

correct = 0
total = 0

# Create a file to store the evaluation results
with open('evaluation_results.txt', 'w') as f:
    with torch.no_grad():  # Disable gradient calculation for evaluation
        for images, labels, file_names in val_dataloader:
            images, labels = images.to(device), labels.to(device)  # Move data to the appropriate device
            outputs = model(images)  # Forward pass
            _, predicted = torch.max(outputs.data, 1)  # Get the index of the max log-probability
            total += labels.size(0)  # Total number of labels
            correct += (predicted == labels).sum().item()  # Count correct predictions
            
            # Write the results to the file
            for i in range(len(file_names)):
                f.write(f'{file_names[i]}: {"with_titlescreen" if predicted[i] == 1 else "without_titlescreen"}\n')

# Calculate and print accuracy
accuracy = 100 * correct / total
print(f'Accuracy of the model on the validation images: {accuracy:.2f}%')
with open('evaluation_results.txt', 'a') as f:
    f.write(f'\nAccuracy: {accuracy:.2f}%')

