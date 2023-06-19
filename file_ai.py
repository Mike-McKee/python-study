import os
import shutil as st

# folder we're taking pics from
downloads_folder = os.path.expanduser("~/Downloads")
# folder we're putting pics into
destination_folder = os.path.expanduser("~/data_study/Canva_pics")



# getting list of files in downloads folder
files = os.listdir(downloads_folder)

# iterates each file

for i in files:
    # checks if file is an image
    if i.endswith("cv.jpeg") or i.endswith("cv.png"):
        source_path = os.path.join(downloads_folder, i)

        destination_path = os.path.join(destination_folder, i)

        st.move(source_path, destination_path)


        print(f"Moved {i} to {destination_path}")
