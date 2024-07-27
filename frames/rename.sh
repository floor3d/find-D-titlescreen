#!/bin/bash

# Check if the correct number of arguments is passed
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 prefix [directory]"
    exit 1
fi

# The prefix to prepend to each file
PREFIX=$1

# The directory to rename files in (default to the current directory if not specified)
DIRECTORY=${2:-.}

# Loop through each file in the directory
for FILE in "$DIRECTORY"/*; do
  # Check if it's a file (skip directories)
  if [ -f "$FILE" ]; then
    # Get the base name of the file (remove the directory part)
    BASENAME=$(basename "$FILE")
    
    # Prepend the prefix to the base name
    NEWNAME="$PREFIX$BASENAME"
    
    # Rename the file
    mv "$FILE" "$DIRECTORY/$NEWNAME"
    
    # Print the new file name
    # echo "Renamed: $FILE -> $DIRECTORY/$NEWNAME"
  fi
done

