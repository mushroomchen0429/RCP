import os
os.system("sudo hciconfig hci0 up")
os.system("sudo hciconfig hci0 leadv 3")
os.system("sudo hciconfig hci0 noscan")
uuid = " 35 04 5C 3B 45 81 4A D8 93 E8 42 89 5D E3 88 6F 00 57 00 5E d8 00"
cmd ="sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 "
#os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 35 04 5C 3B 45 81 4A D8 93 E8 42 89 5D E3 88 6F 00 57 00 5E")
os.system(cmd + uuid)
