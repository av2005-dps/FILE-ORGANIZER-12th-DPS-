import os
import shutil

# folder that we want to clean up
# (change this to whatever folder you want to sort)
directory = os.getcwd() + '\\file_organizer\\files'

# this dictionary tells the program which folder each file type goes in
# if you want to add more file types just add another line
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos'
}

# make sure the folder actually exists first, otherwise it crashes
if not os.path.exists(directory):
    print("Folder not found: " + directory)
    print("Make sure you made a file_organizer/files folder!")
    exit()

count = 0  # keeps track of how many files we moved

# go through every file in the folder
for filename in os.listdir(directory):

    file_path = os.path.join(directory, filename)

    # skip folders, we only want to move files
    if os.path.isdir(file_path):
        continue

    # get the extension (the part after the dot) and make it lowercase
    # so that .JPG and .jpg both work
    extension = filename.split('.')[-1].lower()

    # check if we know this type of file
    if extension in file_extensions:
        folder_name = file_extensions[extension]
    else:
        # if its something we dont know put it in Others
        folder_name = 'Others'

    # make the path for the new folder
    new_folder = os.path.join(directory, folder_name)

    # make the folder if it isnt there yet
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # if a file with the same name is already there, move() would
    # crash (or overwrite) so we add a number to the name instead
    new_path = os.path.join(new_folder, filename)
    number = 1
    while os.path.exists(new_path):
        name = filename.rsplit('.', 1)[0]
        new_path = os.path.join(new_folder, name + '_' + str(number) + '.' + extension)
        number += 1

    # finally move the file
    shutil.move(file_path, new_path)
    print('Moved ' + filename + ' to ' + folder_name)
    count += 1

print('Done! Moved ' + str(count) + ' files.')
