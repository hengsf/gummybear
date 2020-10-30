import pefile
from builtins import any as b_any

def pefile_analy(file):
    pe = pefile.PE(file)
    #
    # For a packed file, raw size would be smaller than virtual size unless it is selective packing
    #
    print("IMAGE_SECTION_HEADER")
    for section in pe.sections:
        print(section.Name.decode('utf-8'))
        print("\tVirtual Address: " + hex(section.VirtualAddress))
        print("\tVirtual Size: " + hex(section.Misc_VirtualSize))
        print("\tRaw Size: " + hex(section.SizeOfRawData))
    print("By comparing Size of Raw Data and Virtual Size may also indicate that the PE file is packed if raw data size is smaller than virtual size")

    import_infor(pe)

def import_infor(pe):
    imported_symbol = None
    import_list = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        imported_symbol = (str(entry.dll))
        import_list.append(imported_symbol)
        print("================================================\n[*] " + imported_symbol + " imports:")
        for x in entry.imports:
            print("\t%s at 0x%08x" % (x.name.decode('utf-8'), x.address))

    possible_out(import_list)

def possible_out(import_list):
    print("\nThese are the imports inside this PE file that are noteworthy: ")
    for item in import_list:
        if ("kernel32.dll" in item.lower()):
           print("\n[**]" + item + ", is a common DLL that gives core function such as access and manipulation of memory, files andhardware")

        if ("advapi32.dll" in item.lower()):
            print("\n[**]" + item+ ", provides more advancedcoreWindows components suchas the ServiceManager and Registry")

        if ("user32.dll" in item.lower()):
            print("\n[**]" + item + ", contains all UI components, like buttons,scroll bars and compoenents for controlling and responding to user actions")

        if("gdi32.dll" in item.lower()):
            print("\n[**]" + item + ", this DLL contains functions for dsiplaying and manipulation graphics")

        if("wininet.dll" in item.lower()):
            print ("\n[**]" + item + ", this DLL contains higher-level networking functions that implement protocols such as FTP, HTTP and NTP. Suggesting some sort of network capability ")

        if("ws2_32.dll" in item.lower()):
            print("\n[**]" + item + ", DLL used to handle network connections. An essential Windows process but can be exploited by malware to create abnormal network activities.")

    print("\n\nFor deeper understanding of what the malware might do, look into the individual function a dynamic link library calls. \nIf this file is packed, what is shown may not be entirely accurate.")
    print("If the file is packed, consider using PEiD to uncover packer used. If none is found, consider using OllyDump to unpack said file.\n")
    print("\n================END of REPORT================")


