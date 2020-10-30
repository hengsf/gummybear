import os
import subprocess

# User input image file name
def with_image():
    disk_input = input("Enter disk file: ")
    return disk_input

# Displays devices and get image
def no_image():
    # Display images
    lsblk_command = 'lsblk -f /dev/sd*'
    os.system(lsblk_command)

    disk_input = input("Enter disk to image: ")
    find_blocksize = 'blockdev --getbsz /dev/' + disk_input
    blocksize = os.popen(find_blocksize).read()

    command = 'dd if=/dev/' + disk_input + ' of=' + disk_input + '.img bs=' + blocksize + ' conv=noerror,sync ' \
                                                                                          'status=progress '
    os.system(command)
    
# Mount image file
def mount_image():
    image_file = input("Creating a mounting point: ")
    command = "mkdir /mnt/gummybear"
    os.system(command)


    command = "mount -o loop " + image_file + " /mnt/gummybear"
    os.system(command)
