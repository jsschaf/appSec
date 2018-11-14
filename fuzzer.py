from subprocess import Popen, PIPE
import string
import base64
import sys
import random
library = string.digits + string.letters;
library += '''_[]{}/\()-+=$%#,.'''
dic = {}


def create_string(s):
    
    s += '''{"'''
    x = random.randint(1,10)
    while (x > 0):
        s += (random.choice(library))
        x = x - 1
    s += ('''":"''')
    y = random.randint(1,10)
    while(y>0):
        s += (random.choice(library))
        y -= 1;
    s += '''}'''
    return s;

def test(s):
    p = Popen('./jsonParser', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    _, err = p.communicate(input = s)
    
    if p.returncode == -11: #or err == "" 
        print  "found input that causes seg fault!"
        print s
        print base64.b64encode(s)
        sys.exit(0)

victim = "{}"
victim += '''{a}'''
victim += '''{"a":1E-4}'''

while(1):
    test(victim)
    victim = create_string(victim)
    test(victim)


