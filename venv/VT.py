import requests
import hashlib
import pefile
import PEA
import APK_A

url = 'https://www.virustotal.com/vtapi/v2/file/report'
api_key = 'da7c3a5c32bed2ec55d2836b19fcf2898ba7383815cdc2ab391b7b52e03f5baf'

def vt_query(): #should put arg/input for file and possibly hash value

    #
    # Compute hash sha256 of files
    #
    hashfile=""
    # filename = input("Enter the input file name: ")
    # sha256_hash = hashlib.sha256()
    # with open('/home/l/Desktop/2202/Assignment/Data/fakeAV_148B76C664F2854E2947AF01160FFA99_LabelReader.apk', "rb") as f:
    #     # Read and update hash string value in blocks of 4K
    #     for byte_block in iter(lambda: f.read(4096), b""):
    #         sha256_hash.update(byte_block)
    #     hashfile = (sha256_hash.hexdigest())

    # Call VT via our api key
    params = {'apikey': api_key , 'resource': hashfile}
    response = requests.get(url, params=params)

    vt_response = response.json()

    md5 = vt_response["md5"]
    sha256 = vt_response["sha256"]
    sha1 = vt_response["sha1"]
    s_date = vt_response["scan_date"]
    positives = vt_response["positives"]
    total = vt_response["total"]

    if (positives == 0):
        print("THIS ITEM LOOKS CLEAN")

    elif (positives > 0):
        print("This particular file with the sha256 hash: " + sha256 + ", has been detected as a potential virus.")
        print("md5: " + md5)
        print("sha1: " + sha1)
        print("Scan Date: " + s_date)
        print("Times detected by common anti-virus: " + str(positives)+ "/" + str(total) +"\n")

        try:
            PEA.pefile_analy("PUT FILE PATH HERE")
        except:
            failure1 = True

        try:
            APK_A.apk_analy("PUT FILE PATH HERE")
        except:
            failure2 = True

        if (failure1 == True and failure2 == True):
            print("This is neither a PE file or .apk file... ending...")

#Remove if this file is not the start of the program
if __name__ == '__main__':
    vt_query()
