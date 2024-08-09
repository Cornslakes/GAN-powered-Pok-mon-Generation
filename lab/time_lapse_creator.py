import cv2
import os
import glob
import time

def create_timelapse(output_folder, output_video_mp4, fps=1):
    # Get list of all PNG files in the output folder
    images = glob.glob(os.path.join(output_folder, "*.png"))

    # Sort images by file creation date
    images.sort(key=os.path.getctime)

    # Check if there are any images
    if not images:
        print("No images found in the output folder.")
        return

    # Read the first image to get the dimensions
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
    video_mp4 = cv2.VideoWriter(output_video_mp4, fourcc_mp4, fps, (width, height))

    for image in images:
        frame = cv2.imread(image)
        
        # Extract epoch from filename
        filename = os.path.basename(image)
        epoch = filename.split('_')[-1].split('.')[0]  # Extracting the epoch number
        
        # Add epoch text to the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'Epoch: {epoch}', (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        
        video_mp4.write(frame)
        time.sleep(1)  # Pause for 1 second between frames

    # Release the video writer
    video_mp4.release()
    print(f"Time-lapse video saved as {output_video_mp4}")

# Example usage
output_folder = "D:/Uni/GAN_powered_Pokemon_Generation/lab/output"
output_video_mp4 = "D:/Uni/GAN_powered_Pokemon_Generation/lab/timelapse.mp4"
create_timelapse(output_folder, output_video_mp4)