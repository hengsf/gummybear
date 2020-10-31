ICT2202 Assignment One
=======
This is our Digital Forensics Assignment for 2020/21 T1 - GummyBear Analyzer Tool.

## Description of this project
1. Automated process of imaging files with working copies provided.
2. Hashing of files to check against a database of hashes for known viruses/ malware. 
3. Hashing of Android Application Package (APK).

## Demo
youtube link and/or images here

## Technologies Used
- Android Malware Zoo:
  https://github.com/ashishb/android-malware
- Self-coded malware
- VirusTotal
- Androguard
- Python modules: 

## Installation
- Clone the repository onto an Ubuntu machine. 
- Install all required module using the "requirements.txt" file with the commnad: pip3 install -r requirements.txt

## Prerequisites
- User has to run the Python script as a root user.
- User must be using python3.
- User must install sleuthkit.
- Automount must be disabled.

## How to Run This
- Navigate to the folder containing the CLI.py file.
- Run as root with the following command to start the program: python3 CLI.py

## Limitations
- Imaging of disks will vary based on disk size.
- Hashing of files for verification with the API is limited to four queries per minute.
