import cv2
import os
import sys

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video file opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Save each frame as an image file
        frame_filename = os.path.join(output_folder, f"{os.path.splitext(video_path)[0]}_frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    cap.release()
    print(f"Extracted {frame_count} frames from the video.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python framify.py <video_path>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    output_folder = "../frames/" + os.path.splitext(video_path)[0] + "_frames"
    
    extract_frames(video_path, output_folder)
