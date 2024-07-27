import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
dataset_dir = 'frames'
train_dir = 'frames/train'
val_dir = 'frames/val'

# Create directories for training and validation sets
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(os.path.join(train_dir, 'with_titlescreen'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'without_titlescreen'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'with_titlescreen'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'without_titlescreen'), exist_ok=True)

# Function to split data
def split_data(src_dir, train_dir, val_dir, test_size=0.2):
    # Get list of all files
    files = os.listdir(src_dir)
    train_files, val_files = train_test_split(files, test_size=test_size)

    # Copy files to the train and val directories
    for file in train_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(train_dir, file))

    for file in val_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(val_dir, file))

# Split the 'with_titlescreen' data
split_data(os.path.join(dataset_dir, 'with_titlescreen'),
           os.path.join(train_dir, 'with_titlescreen'),
           os.path.join(val_dir, 'with_titlescreen'))

# Split the 'without_titlescreen' data
split_data(os.path.join(dataset_dir, 'without_titlescreen'),
           os.path.join(train_dir, 'without_titlescreen'),
           os.path.join(val_dir, 'without_titlescreen'))

print('Data split completed.')

