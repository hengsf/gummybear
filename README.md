ICT2202 Assignment One
=======
Hi there! This is our Digital Forensics Assignment for 2020/21 T1 - GummyBear Analyzer Tool. We are tasked to design and develop a technical solution for a problem in digital forensics. The amount of files generated for a malware sample could become tremendously huge, inspecting the hard disk requires an extensive effort. There, we focusing on a security tool for analysts and aim to automate some initial part of malware analysis with the help of virus databases such as VirusTotal.

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
**Step 5:** Disable automount with the following command:
```
gsettings set org.gnome.desktop.media-handling automount false
```
```
gsettings set org.gnome.desktop.media-handling automount-open false 
```
<i> restart your machine </i>

Alternatively, install dconf-editor:
```
apt install dconf-editor
```
Open dconf-editor > org > gnome > desktop > media-handling, turn off <b>automount</b> and <b>automount-open</b> and restart your machine

**Step 6:** Navigate to the foldercontaining the CLI.py file and Run as root with the following command to start the program:
```
python3 CLI.py
```

## Limitations
- Imaging of disks will vary based on disk size.
- Hashing of files for verification with the API is limited to <b> four queries per minute </b>.

## References/Technologies Used
- Android Malware Zoo https://github.com/ashishb/android-malware
- Self-coded malware
- VirusTotal https://developers.virustotal.com/reference#file-report
- Androguard https://pypi.org/project/androguard/
- Python modules/libraries/api: 
    * collections https://docs.python.org/3/library/collections.html
    * os https://docs.python.org/3/library/os.html
    * sys https://docs.python.org/3/library/sys.html
    * struct https://docs.python.org/3/library/struct.html
    * mmap https://docs.python.org/3.0/library/mmap.html
    * hashlib https://docs.python.org/3/library/hashlib.html
    * regex https://docs.python.org/3/library/re.html
    * pyInquirer https://pypi.org/project/PyInquirer/
    * pyfiglet https://pypi.org/project/pyfiglet/
    * requests https://pypi.org/project/requests/
    * pefile https://pypi.org/project/pefile/

## Demo/User Guide
youtube link and/or images here

## Authors
- Lim Zhi Hong @LZHcoroda https://github.com/LZHcoroda
- Lee Jia Ying @jyyyyyyyyy https://github.com/jyyyyyyyyy
- Muhammad Rawandy Bin Rosle @RawandyRosle https://github.com/RawandyRosle
- Heng Sinn Fei @hengsf https://github.com/hengsf
- Heng Pei Min @hengpeimin https://github.com/hengpeimin
