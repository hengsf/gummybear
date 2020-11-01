import requests
import hashlib
import pefile
import PEA
import APK_A
import sys

# Warnings for md5 etc because only can query 4 per minute.
sys.tracebacklimit = 0

url = 'https://www.virustotal.com/vtapi/v2/file/report'
api_key = 'da7c3a5c32bed2ec55d2836b19fcf2898ba7383815cdc2ab391b7b52e03f5baf'

# Input for option 3.
def get_path():
    in_val = input("Enter full path of file: ")
    vt_query(in_val)

# Input for option 1 and 2.
def get_path_2():
    in_val = input("Enter name of file: ")
    in_val = '/mnt/gummybear/' + in_val
    print('Choosing: ' + in_val)
    vt_query(in_val)   
      
def vt_query(file):
    failure1 = False
    failure2 = False

    # Compute hash sha256 of files
    hashfile = ""
    sha256_hash = hashlib.sha256()

    try:
        with open(file, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            hashfile = (sha256_hash.hexdigest())
    except:
        print("Wrong folder/ file name. Please run this program again.")
        exit()

    # Call VT via our api key
    params = {'apikey': api_key , 'resource': hashfile}
    response = requests.get(url, params=params)

    vt_response = response.json()
    
    if (vt_response.get('response_code') == 0):
        print(
            "This file has not been scanned due to the upload limitations on VirusTotal.\nPlease run this application again in two minutes..\n")
        exit()

    md5 = vt_response["md5"]
    sha256 = vt_response["sha256"]
    sha1 = vt_response["sha1"]
    s_date = vt_response["scan_date"]
    positives = vt_response["positives"]
    total = vt_response["total"]

    if (positives == 0):
        print("THIS ITEM LOOKS CLEAN")

    elif (positives > 0):
        print("\n\n================START of REPORT================\nThis particular file has been identified as a malicious file.")
        print("sha256: " + sha256)
        print("md5: " + md5)
        print("sha1: " + sha1)
        print("Scan Date: " + s_date)
        print("Times detected by common anti-virus: " + str(positives)+ "/" + str(total) +"\n")

        try:
            PEA.pefile_analy(file)
        except:
            failure1 = True

        try:
            APK_A.apk_analy(file)
        except:
            failure2 = True

        if (failure1 == True and failure2 == True):
            print("This is neither a PE file or .apk file... ending...")
            print("\n================END of REPORT================")
