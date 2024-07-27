#!/bin/bash

# Ensure the script is executed with the correct number of arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <directory> <start_frame> <end_frame>"
    exit 1
fi

# Define the directory containing the image files
src_dir=$1

# Define the frame range
start_frame=$2
end_frame=$3

# Define the destination directories
dest_dir1="${src_dir}/with_titlescreen"
dest_dir2="${src_dir}/without_titlescreen"

# Create the destination directories
mkdir -p "$dest_dir1"
mkdir -p "$dest_dir2"

# Loop through the files in the source directory
for file in "$src_dir"/OP*frame_*.jpg; do
    # Extract the frame number from the filename
    frame_number=$(basename "$file" .jpg | cut -d'_' -f3)

    # Determine the destination directory based on the frame number
    if [ "$frame_number" -ge "$start_frame" ] && [ "$frame_number" -le "$end_frame" ]; then
        mv "$file" "$dest_dir1"
    else
        mv "$file" "$dest_dir2"
    fi
done

echo "Files have been moved successfully."
