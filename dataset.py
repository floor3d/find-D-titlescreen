import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

# Custom dataset class for loading images
class TitleScreenDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        # Initialize the dataset with the root directory and optional transformations
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []

        # Load images and labels from the specified directories
        for label, subdir in enumerate(['without_titlescreen', 'with_titlescreen']):
            subdir_path = os.path.join(root_dir, subdir)
            for file_name in os.listdir(subdir_path):
                self.images.append((os.path.join(subdir_path, file_name), file_name))
                self.labels.append(label)

    def __len__(self):
        # Return the total number of samples
        return len(self.images)

    def __getitem__(self, idx):
        # Get a single sample (image and label) by index
        img_path, file_name = self.images[idx]
        image = Image.open(img_path).convert('RGB')  # Convert image to RGB
        label = self.labels[idx]  # Get the corresponding label
        if self.transform:
            image = self.transform(image)  # Apply transformations if any
        return image, label, file_name

# Define transformations to apply to each image (resize and convert to tensor)
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

