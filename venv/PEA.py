import pefile
from builtins import any as b_any

pe =  pefile.PE("/home/l/Desktop/2202/Assignment/Data/P_malware.exe")

def import_infor():
    imported_symbol = "var to hold import names"
    import_list = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
      imported_symbol = (str(entry.dll))
      import_list.append(imported_symbol)

    # print(pe.get_warnings())
    # print(pe.show_warnings())
    # print(import_list)

    possible_out(import_list)

def possible_out(import_list):
    for item in import_list:
        if ("kernel32.dll" in item.lower()):
           print("This Dynamic-link library: " + item + ", is a common DLL that gives core function such as access and manipulation of memory, files andhardware")

        if ("ADVAPI32.dll" in item):
            print("Provides more advancedcoreWindows components suchas the ServiceManager and Registry")

        if ("USER32.dll" in item):
            print("Contains all UI components, like buttons,scroll bars and compoenents for controlling and responding to user actions")

        if("GDI32.dll" in item):
            print("This DLL contains functions for dsiplaying and manipulation graphics")

        # if("NTDLL.DLL")

if __name__ == "__main__":
    import_infor()


