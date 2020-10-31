ICT2202 Assignment One
=======
This is our Digital Forensics Assignment for 2020/21 T1 - GummyBear Analyzer Tool.

## Description of this project
1. Automated process of imaging files with working copies provided.
2. Hashing of files to check against a database of hashes for known viruses/ malware. 
3. Hashing of Android Application Package (APK).

## Prerequisites
- User has to run the Python script as a <b> root user </b>.
- User must be using python3.
- User must install sleuthkit.
- Automount must be disabled.

## Installation & How to Run
**Step 1:** Clone the repository onto an Ubuntu machine. 

**Step 2:** Install all required module using the "requirements.txt" file with the following command:
```
pip3 install -r requirements.txt
```
**Step 3:** Check if you have python3 installed with the following command:
```
python3 --version
```
If not, install python3:
```
apt install python3
```
<i> Please install version 3.6.9 and above </i>

**Step 4:** Install sleuthkit using the following command:
```
apt install sleuthkit
```
**Step 5:** Disable automount with the following commands:
```
gsettings set org.gnome.desktop.media-handling automount false
```
```
gsettings set org.gnome.desktop.media-handling automount-open false 
```
<i> restart your machine </i>

**Step 6:** Navigate to the foldercontaining the CLI.py file and Run as root with the following command to start the program:
```
python3 CLI.py
```

## Limitations
- Imaging of disks will vary based on disk size.
- Hashing of files for verification with the API is limited to four queries per minute.

## References/Technologies Used
- Android Malware Zoo https://github.com/ashishb/android-malware
- Self-coded malware
- VirusTotal https://developers.virustotal.com/reference#file-report
- Androguard https://pypi.org/project/androguard/
- Python modules/libraries/api: 
    https://docs.python.org/3/library/collections.html
    https://docs.python.org/3/library/os.html
    https://docs.python.org/3/library/sys.html
    https://docs.python.org/3/library/struct.html
    https://docs.python.org/3.0/library/mmap.html
    https://docs.python.org/3/library/hashlib.html
    https://docs.python.org/3/library/re.html
    https://pypi.org/project/PyInquirer/
    https://pypi.org/project/pyfiglet/
    https://pypi.org/project/requests/
    https://pypi.org/project/pefile/

## Demo/User Guide
youtube link and/or images here

## Authors
Lim Zhi Hong @LZHcoroda
Lee Jia Ying @jyyyyyyyyy
Muhammad Rawandy Bin Rosle @RawandyRosle
Heng Sinn Fei @hengsf
Heng Pei Min @hengpeimin
