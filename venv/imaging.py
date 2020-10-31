import os
import subprocess

# User with an image file
def with_image():
    disk_input = input("Enter path of disk file: ")

    # Get hash of before
    command = 'sha1sum ' + disk_input
    hash_before = os.popen(command).read()

    # Create a working copy of image
    txt = '/home/l/Desktop/ForensicGUI/venv/sdb3.img'
    file_name = txt.split("/")[-1].split(".")[0]

    command = 'cp ' + disk_input + ' ' + file_name + '_backup.img'
    os.system(command)

    # Get hash of after
    command = 'sha1sum ' + file_end + '_backup.img'
    hash_after = os.popen(command).read()

    if hash_before[:40] == hash_after[:40]:
        dir = os.popen('pwd').read()
        statement = dir + file_name + '_backup.img'
        print("A backup image file has been created at: " + statement)

    else:
        print('Hash of image does not match original, run the program again.')
        command = ' rm ' + file_name + '_backup.img'
        os.system(command)
        exit()

   # processing(statement)

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
    blocksize = os.popen(find_blocksize).read()

    # Creating an image
    command = 'dd if=' + disk_dev + ' of=' + disk_img + ' bs=' + blocksize + ' conv=noerror,sync ' \
                                                                                          'status=progress '

    os.system(command)

    dir = os.popen('pwd').read()
    statement = 'An image has been create: ' + dir + disk_img
    print(statement)

    # Get hash of after
    command = 'sha1sum ' + disk_img
    hash_after = os.popen(command).read()

    # Compare hash
    if hash_before[:40] == hash_after[:40]:
        # Create a working copy of image
        command = 'cp ' + disk_img + ' ' + disk_input + '_backup.img'
        os.system(command)
        statement = dir + disk_input + '_backup.img'
        print("A backup image file has been created at: " + statement)

    else:
        print('Hash of image does not match original, run the program again.')
        command = 'rm ' + dir + disk_img
        os.system(command)
        command = 'rm ' + dir + disk_input + '_backup.img'
        os.system(command)
        exit()

# # User with an image file
# def with_image():
#     disk_input = input("Enter path of disk file: ")

#     # Get hash of before
#     command = 'sha256 sum ' + disk_input
#     hash_before = os.popen(command).read()

#     # Create a working copy of image
#     command = disk_input + '.split("/")[-1]'
#     file_name = os.popen(command).read()

#     command = 'cp ' + disk_input + ' ' + file_name + '_backup.img'
#     os.system(command)

#     # Get hash of after
#     command = 'sha256 sum ' + file_name + '_backup.img'
#     hash_after = os.popen(command).read()

#     if hash_before == hash_after:
#         dir = os.popen('pwd').read()
#         statement = dir + disk_input + '_backup.img'
#         print("A backup image file has been created at: " + statement)

#     else:
#         print('Hash of image does not match original, run the program again.')
#         command = ' rm ' + disk_img + '_backup.img'
#         os.system(command)


# # User without an image file
# def no_image():
#     # Display devices
#     lsblk_command = 'lsblk -f /dev/sd*'
#     os.system(lsblk_command)

#     disk_input = input("Enter disk to image (sd*): ")

#     # Path to disks
#     disk_dev = '/dev/' + disk_input
#     disk_img = disk_input + '.img'

#     # Get hash of before
#     command = 'sha256 sum ' + disk_input
#     hash_before = os.popen(command).read()

#     find_blocksize = 'blockdev --getbsz ' + disk_dev
#     blocksize = os.popen(find_blocksize).read()

#     # Creating an image
#     command = 'dd if=' + disk_dev + ' of=' + disk_img + ' bs=' + blocksize + ' conv=noerror,sync ' \
#                                                                                           'status=progress '

#     os.system(command)

#     dir = os.popen('pwd').read()
#     statement = 'An image has been create: ' + dir + disk_img
#     print(statement)

#     # Get hash of after
#     command = 'sha256 sum ' + disk_img
#     hash_after = os.popen(command).read()

#     # Compare hash
#     if hash_before == hash_after:
#         # Create a working copy of image
#         command = 'cp ' + disk_img + disk_input + '_backup.img'
#         os.system(command)
#         statement = dir + disk_input + '_backup.img'
#         print("A backup image file has been created at: " + statement)

#     else:
#         print('Hash of image does not match original, run the program again.')
#         command = 'rm ' + dir + disk_img
#         os.system(command)
#         command = 'rm ' + dir + disk_img + '_backup.img'
#         os.system(command)

# # Mount image file
# def mount_image():
#     image_file = input("Creating a mounting point: ")
#     command = 'mkdir /mnt/gummybear'
#     os.system(command)

#     command = 'mount -o loop ' + image_file + ' /mnt/gummybear'
#     os.system(command)


# # Print directories to choose from
# def find_directories():
#     # Filtering of directories with grep and regular expression
#     # Extend file obmitted with NTFS (not applicable for scanning)
#     # OrphanFile no within project scanning scope
#     regex = ' | grep -oP "(?<=(:\t)).*" | grep -vwE "OrphanFiles" | grep -vwE "Extend"'
#     image_file = input("Img location: ")

#     command = 'fls -D -u ' + image_file + regex
#     os.system(command)


# def find_files():
#     image_file = input("Img location: ")
#     regex = ' | grep -i -w "Work" | grep -w "r/r" | grep -oP "(?<=(:\t)).*" '
#     command = 'fls -r -p  ' + image_file + regex
#     os.system(command)

# # Uncomment this when testing in this file
# find_directories()
# find_files()
