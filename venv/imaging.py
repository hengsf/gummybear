import os
import subprocess
import backend

# User with an image file
def with_image():
    disk_input = input("Enter full path of disk file: ")

    # Get hash of before
    command = 'sha1sum ' + disk_input
    hash_before = os.popen(command).read()

    # Create a working copy of image
    file_name = disk_input.split("/")[-1].split(".")[0]

    command = 'cp ' + disk_input + ' ' + file_name + '_backup.img'
    os.system(command)

    # Get hash of after
    command = 'sha1sum ' + file_name + '_backup.img'
    hash_after = os.popen(command).read()

    # File paths
    dir = os.popen('pwd').read().rstrip()
    statement = dir + '/' + file_name + '_backup.img'
        
    if hash_before[:40] == hash_after[:40]:
        
        print("A backup image file has been created at: " + statement)

    else:
        print('Hash of image does not match original, run the program again.')
        command = ' rm ' + file_name + '_backup.img'
        os.system(command)
        exit()

    backend.processing(statement)

# User without an image file
def no_image():
    # Display devices
    lsblk_command = 'lsblk -f /dev/sd*'
    os.system(lsblk_command)

    disk_input = input("Enter disk to image (sd*): ")

    # Path to disks
    disk_dev = '/dev/' + disk_input
    disk_img = disk_input + '.img'

    # Get hash of before
    command = 'sha1sum ' + disk_dev
    hash_before = os.popen(command).read()

    find_blocksize = 'blockdev --getbsz ' + disk_dev
    blocksize = os.popen(find_blocksize).read().rstrip()

    # Creating an image
    command = 'dd if=' + disk_dev + ' of=' + disk_img + ' bs=' + blocksize + ' conv=noerror,sync ' \
                                                                                          'status=progress '

    os.system(command)

    dir = os.popen('pwd').read().rstrip()
    statement = 'An image has been create: ' + dir + '/' + disk_img
    print(statement)

    # Get hash of after
    command = 'sha1sum ' + disk_img
    hash_after = os.popen(command).read()

    # Locations
    backup_file = disk_input + '_backup.img'
    backup_location = dir + disk_input + '_backup.img'

    # Compare hash
    if hash_before[:40] == hash_after[:40]:
        # Create a working copy of image
        command = 'cp ' + disk_img + ' ' + backup_file
        os.system(command)
        print("A backup image file has been created at: " + backup_location)

    else:
        print('Hash of image does not match original, run the program again.')
        command = 'rm ' + dir + disk_img
        os.system(command)
        command = 'rm ' + backup_location
        os.system(command)
        exit()

    backend.processing(backup_location)
