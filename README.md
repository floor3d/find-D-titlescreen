# One Piece Titlescreen Finder
### What this is
This project takes a One Piece episode and tries to find the first instance of the title screen.

It is highly underdeveloped so far and I will be automating more parts of it in the future.

**I used ChatGPT for most all of this. Lord forgive me.**

### How to

0. Download a One Piece episode 
1. Use `framify.py` to split the video into single frames
2. Single out all of the frames that are a titlescreen, and remember the start and end, i.e. frame X to frame Y are all titlescreen images
3. Run `segregate.sh` to put all of the titlescreen frames (frame X to frame Y) in a
with_titlescreen directory and the rest of them in a without_titlescreen directory
4. Amalgamate all your episodes' files into a with_titlescreen and without_titlescreen folder inside frames/
5. run `split_data.py` to split data into a train and validation dataset (note: you could alternatively modify this script to create with_titlescreen
dir and without_titlescreen dir automatically so that there is less manual labor, therefore removing step 4)
6. run `train.py`
7. To test, run `predict.py` on a frame of your choice or `predict_first_titlescreen.py` on a bunch of frames of your choice
8. To find the timestamp of the predicted frame, run `find-timestamp-for-frame/find-timestamp-for-frame.py`
