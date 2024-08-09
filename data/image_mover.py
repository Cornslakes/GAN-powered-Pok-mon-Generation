import os
import shutil

# Path where all picture lie in
base_path = "./data"
i = 0

# Create a folder for all generations
target_folder = os.path.join(base_path, "All_Generations", "pics")
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Iterate over all folders in the base path
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # Check if the current folder is a directory
    if os.path.isdir(folder_path):
        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".jpg"):
                file_path = os.path.join(folder_path, file_name)
                
                # Copy the file to the target folder
                shutil.copy(file_path, os.path.join(target_folder, file_name))
                i += 1
                print(f"Copied {file_name} to {target_folder}.")

print(f"All {i} files have been moved successfully!")
