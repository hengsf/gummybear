# from androguard.misc import AnalyzeAPK, AnalyzeDex
from androguard import misc
from androguard import session
from androguard.core.bytecodes.apk import APK

def apk_analy(file):
    apk_file = file

    apkf, b, dx = misc.AnalyzeAPK(apk_file)

    #get_APK name
    name = apkf.get_app_name()
    get_app_name(name)

    #get_permission
    permissions = apkf.get_permissions()
    get_permissions(permissions)

    #find strings inside one or multiple DEX files
    strings = dx.get_strings()
    get_network_IOC(strings)

    # Signature
    look_at_cert(apkf)

def get_app_name(app_name):
        print("/////////////////////////////////////////")
        print("/// ANDROID APP NAME: " + app_name)
        print("/////////////////////////////////////////")


def get_permissions(pm):
    perm_dict = {
        "android.permission.CALL_PHONE" : "Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call.",
        "android.permission.INTERNET" : "Allows applications to open network sockets.",
        "android.permission.WRITE_EXTERNAL_STORAGE" : "Allows an application to write to external storage.",
        "android.permission.READ_EXTERNAL_STORAGE" : "Allows an application to read from external storage.",
        "android.permission.READ_CONTACTS" : "Allows an application to read the user's contacts data.",
        "android.permission.READ_PHONE_STATE" : "Allows read only access to phone state.",
        "android.permission.PROCESS_OUTGOING_CALLS" : "Allows an application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether.",
        "android.permission.RECEIVE_SMS" : "Allows an application to receive SMS messages.",
        "android.permission.RECEIVE_BOOT_COMPLETED" : "Allows an application to receive the ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting.",
        "android.permission.SEND_SMS" : "Allows an application to send SMS messages. ",
        "android.permission.CAMERA" : "Required to be able to access the camera device. ",
        "android.permission.GET_ACCOUNTS" : "Allows access to the list of accounts in the Accounts Service.",
        "android.permission.PROCESS_OUTGOING_CALLS" : "Allows an application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether. ",
        "android.permission.READ_CALENDAR" : "Allows an application to read the user's calendar data. ",
        "android.permission.READ_CALL_LOG": "Allows an application to read the user's call log. ",
        "android.permission.READ_PHONE_NUMBERS": "Allows read access to the device's phone number(s). This is a subset of the capabilities granted by READ_PHONE_STATE but is exposed to instant applications. ",
        "android.permission.READ_SMS": "Allows an application to read SMS messages. ",
        "android.permission.RECEIVE_MMS": "Allows an application to monitor incoming MMS messages.",
        "android.permission.RECORD_AUDIO": "Allows an application to record audio. ",
        "android.permission.RECEIVE_WAP_PUSH": "Allows an application to receive WAP push messages.",
        "android.permission.WRITE_CALENDAR": "Allows an application to write the user's calendar data. ",
        "android.permission.WRITE_CALL_LOG": "Allows an application to write (but not read) the user's call log data. ",
        "android.permission.WRITE_CONTACTS": "Allows an application to write the user's contacts data. "
    }
    print("\n/////////////////////////////////////////"
          "\n///Listed here are permission(s) that may be dangerous if used by the malware:"
          "\n/////////////////////////////////////////")

    for existing_perm in pm:
        for key in perm_dict:
            if (existing_perm == key):
                print (key + " : \t" + perm_dict.get(key))


def get_network_IOC(string_parse):
    print("================================================\n/////////////////////////////////////////"
          "\n///Possible Network Indicator of Compromise: "
          "\n/////////////////////////////////////////")

    for network_IOC in string_parse:
        s = str(network_IOC)
        if "http:" in s.lower():
            print(network_IOC)
        elif ".org" in s.lower():
            print(network_IOC)
        elif "www." in s.lower():
            print(network_IOC)
        elif ".com" in s.lower():
            print(network_IOC)

def look_at_cert(apk_a):
    if apk_a.is_signed():
        # Test if signed v1 or v2 or both
        print("APK is signed with: {}".format("both" if apk_a.is_signed_v1() and
                                                        apk_a.is_signed_v2() else "v1" if apk_a.is_signed_v1() else "v2"))

        for cert in apk_a.get_certificates():
            # Each cert is now a asn1crypt.x509.Certificate object
            # From the Certificate object, we can query stuff like:
            print(cert.issuer.human_friendly)  # the sha1 fingerprint
            print("Certificate signature date: " + cert.not_valid_before)
            print("Certificate signature expiry date: " + cert.not_valid_after)

