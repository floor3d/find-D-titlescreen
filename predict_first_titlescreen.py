import torch
from torchvision import transforms
from PIL import Image
import sys
from model import SimpleCNN
import os

# Function to load and preprocess the image
def load_images_from_directory(directory, batch_size=32):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])
    images = []
    image_paths = []

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path).convert('RGB')
            image = transform(image)
            images.append(image)
            image_paths.append(image_path)

    # Batch images
    for i in range(0, len(images), batch_size):
        yield images[i:i + batch_size], image_paths[i:i + batch_size]

# Function to make predictions
def predict(model, images):
    # Stack images to create a batch
    images = torch.stack(images)
    
    # Move the batch to the same device as the model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    images = images.to(device)

    # Put the model in evaluation mode
    model.eval()

    # Disable gradient calculation
    with torch.no_grad():
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
    
    return predicted

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict_first_with_titlescreen_batched.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]

    # Load the trained model
    model = SimpleCNN()
    model.load_state_dict(torch.load('titlescreen_model.pth'))
    model = model.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    # Iterate through batches of images
    for batch_images, batch_paths in load_images_from_directory(directory):
        predictions = predict(model, batch_images)
        class_names = ['without_titlescreen', 'with_titlescreen']
        
        for i, prediction in enumerate(predictions):
            result = class_names[prediction.item()]
            image_path = batch_paths[i]
            # print(f'The model predicts that the image {image_path} is: {result}')
            if result == "with_titlescreen":
                print(f'First instance of "with_titlescreen" found: {image_path}')
                sys.exit(0)
    
    print('No instance of "with_titlescreen" found in the provided images.')

