import os
import fnmatch
import shutil

#this was done with a good bit of chatgpt, if the brackets below is crossed it means I've read through to validate that the code is actually doing what we want it to
#()

def find_png_files_with_underscore(root_folder):
    png_files = []
    # Walk through the directory and all its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            # Match files that have an underscore and a .png extension
            if fnmatch.fnmatch(filename, '*_*.png'):
                png_files.append(os.path.join(dirpath, filename))
    return png_files

def copy_files_to_new_folder(files, new_folder):
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    
    for file in files:
        shutil.copy(file, new_folder)

# script is in the same folder as the "Dat" folder
current_dir = os.path.dirname(os.path.abspath(__file__))
dat_folder = os.path.join(current_dir, 'Dat')  # Path to "Dat" folder
new_folder_path = os.path.join(current_dir, 'pngCopyOnly')  # Path to "pngCopyOnly" folder

# Find all matching .png files with an underscore in their name from the "Dat" folder
result = find_png_files_with_underscore(dat_folder)

# Copy them to the "pngCopyOnly" folder
copy_files_to_new_folder(result, new_folder_path)

print(f"Files have been copied to {new_folder_path}")
