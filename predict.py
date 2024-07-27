import torch
from torchvision import transforms
from PIL import Image
import sys
from model import SimpleCNN

# Function to load and preprocess the image
def load_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])
    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension
    return image

# Function to make a prediction
def predict(model, image_path):
    # Load the image
    image = load_image(image_path)
    
    # Move the image to the same device as the model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    image = image.to(device)

    # Put the model in evaluation mode
    model.eval()

    # Disable gradient calculation
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs.data, 1)
    
    # Map the prediction to the class name
    class_names = ['without_titlescreen', 'with_titlescreen']
    prediction = class_names[predicted.item()]
    
    return prediction

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]

    # Load the trained model
    model = SimpleCNN()
    model.load_state_dict(torch.load('titlescreen_model.pth'))
    model = model.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    # Make a prediction
    prediction = predict(model, image_path)
    print(f'The model predicts that the image is: {prediction}')

