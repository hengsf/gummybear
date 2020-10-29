import requests
import hashlib

url = 'https://www.virustotal.com/vtapi/v2/file/report'
api_key = 'da7c3a5c32bed2ec55d2836b19fcf2898ba7383815cdc2ab391b7b52e03f5baf'

def vt_query(): #should put arg/input

    #
    # Compute hash sha256 of files
    #
    hashfile=""
    # filename = input("Enter the input file name: ")
    sha256_hash = hashlib.sha256()
    with open('/home/l/Desktop/2202/Assignment/Data/fakeAV_148B76C664F2854E2947AF01160FFA99_LabelReader.apk', "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        hashfile = (sha256_hash.hexdigest())

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

    print(md5)


if __name__ == '__main__':
    vt_query()


"""EXAMPLE"""
"""
{
 'response_code': 1,
 'verbose_msg': 'Scan finished, scan information embedded in this object',
 'resource': '99017f6eebbac24f351415dd410d522d',
 'scan_id': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c-1273894724',
 'md5': '99017f6eebbac24f351415dd410d522d',
 'sha1': '4d1740485713a2ab3a4f5822a01f645fe8387f92',
 'sha256': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c',
 'scan_date': '2010-05-15 03:38:44',
 'permalink': 'https://www.virustotal.com/file/52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c/analysis/1273894724/',
 'positives': 40,
 'total': 40,
 'scans': {
   'nProtect': {
     'detected': true, 
     'version': '2010-05-14.01', 
     'result': 'Trojan.Generic.3611249', 
     'update': '20100514'
   },
   'CAT-QuickHeal': {
     'detected': true, 
     'version': '10.00', 
     'result': 'Trojan.VB.acgy', 
     'update': '20100514'
   },
   'McAfee': {
     'detected': true, 
     'version': '5.400.0.1158', 
     'result': 'Generic.dx!rkx', 
     'update': '20100515'
   },
   'TheHacker': {
     'detected': true, 
     'version': '6.5.2.0.280', 
     'result': 'Trojan/VB.gen', 
     'update': '20100514'
   },   
   'VirusBuster': {
    'detected': true,
     'version': '5.0.27.0',
     'result': 'Trojan.VB.JFDE',
     'update': '20100514'
   }
 }
}
"""