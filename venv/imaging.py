import os
import subprocess

def with_image():
    disk_input = input("Enter disk file: ")
    return disk_input

def no_image():
    # Display images
    lsblk_command = 'lsblk'
    os.system(lsblk_command)

    disk_input = input("Enter disk to image: ")
    find_blocksize = 'blockdev --getbsz /dev/' + disk_input
    blocksize = os.popen(find_blocksize).read()
    print(blocksize)

    command = 'dd if=/dev/' + disk_input + ' of=' + disk_input + '.img bs=' + blocksize + ' conv=noerror,sync ' \
                                                                                          'status=progress '
    print(command)
    os.system(command)