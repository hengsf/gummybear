import os
import subprocess
import VT

# Mount image file
def mount_image(image_file):
    print("Creating a mounting point at /mnt/gummybear")
    command = 'mkdir /mnt/gummybear'
    os.system(command)

    command = 'mount -o loop ' + image_file + ' /mnt/gummybear'
    os.system(command)

    print("Image has been mounted at /mnt/gummybear. \n")


# Print directories to choose from
def find_directories(image_file):
    # Filtering of directories with grep and regular expression
    # Extend file obmitted with NTFS (not applicable for scanning)
    # OrphanFile no within project scanning scope
    regex = ' | grep -oP "(?<=(:\t)).*" | grep -vwE "OrphanFiles" | grep -vwE "Extend"'
    command = 'fls -D -u ' + image_file + regex
    print("Printing list of directories: \n")
    os.system(command)

    find_files(image_file)


def find_files(image_file):
    folder = input("Enter folder to view: ")
    regex = ' | grep -i -w "' + folder + '" | grep -w "r/r" | grep -oP "(?<=(:\t)).*" '
    command = 'fls -r -p  ' + image_file + regex
    os.system(command)
    VT.get_path()


def processing(image_file):
    mount_image(image_file)
    find_directories(image_file)

# Uncomment this when testing in this file

# mount_image()
# find_directories()
# find_files()
