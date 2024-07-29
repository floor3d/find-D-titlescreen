import cv2
import sys

def get_video_fps(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None

    # Get the frames per second (FPS)
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Release the video file
    video.release()
    
    return fps

# Example usage
video_path = sys.argv[1]
frame_in_question = sys.argv[2].split("_")
number = int(''.join(char for char in frame_in_question[len(frame_in_question) - 1] if char.isdigit()))
fps = get_video_fps(video_path)

if fps is not None:
    print(f"Frames per second (FPS): {fps}")
    seconds = int(number / float(fps))
    m, s = divmod(seconds, 60)
    print(f"Timestamp: {m}:{s}")

