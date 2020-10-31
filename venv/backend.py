import os
import subprocess
import VT

# Mount image file for processing
def mount_image(image_file):
    print("Creating a mounting point at /mnt/gummybear")
    command = 'mkdir /mnt/gummybear'
    os.system(command)

    try:
        command = 'mount -o loop ' + image_file + ' /mnt/gummybear'
        os.system(command)
        print("Image has been mounted at /mnt/gummybear. \n")
        
     except:
        print("WARNING: Mount point in use, unmounting in progress. Exit mount point if required.")
        command = 'umount /dev/gummybear'
        os.system(command)
        mount_image(image_file)
       
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
    
# Print all files in folder (including files in subfolders)
def find_files(image_file):
    folder = input("Enter folder to view: ")
    regex = ' | grep -i -w "' + folder + '" | grep -w "r/r" | grep -oP "(?<=(:\t)).*" '
    command = 'fls -r -p  ' + image_file + regex
    os.system(command)
    VT.get_path_2()
    
# Main event caller
def processing(image_file):
    mount_image(image_file)
    while(1):
        find_directories(image_file)
