#!/usr/bin/python
import random
import string
import base64
import sys
import json
import subprocess
import os


found = False
size = 1
pchar = string.ascii_letters + string.digits
p_bool = ['true', 'false']
letters = string.ascii_letters
nums = string.digits

def seg_string():
    key = ''.join(random.choice(letters))
    value = ''.join((random.choice(pchar) for i in range (random.randint(0, size))))
    attempt = '{\"' + key + '\":\"' + value * size + '\"}'
#    print attempt
    return attempt

def seg_int():
    key = ''.join(random.choice(letters))
    value = ''.join((random.choice(nums) for i in range (random.randint(0, size))))
    attempt = "{\"" + key + "\":" + value * size + "}"
#    print attempt
    return attempt

def seg_array():
    key = ''.join(random.choice(letters))
    value = []
    for i in range (random.randint(0, size^2)): 
        value.append(random.choice(string.printable))
#    attempt = "{\"" + key + "\":" + value + "}"
    print value
    attempt = json.dumps(key, str(value))
    print attempt
    return attempt

def seg_object():
    pass

    
def seg_bool():
    # Flipping a coin 5 times would give you a 96% confidence interval you would get one of either heads or tails
    key = ''.join(random.choice(letters))
    value = ''.join((random.choice(p_bool) for i in range(random.randint(1, 5))))
    attempt = "{\"" + key + "\":" + value * size + "}"
#    print attempt
    return attempt

def seg_null():
    key = ''.join(random.choice(letters))
    value = ''.join(('\x00' for i in range (random.randint(0, size))))
    attempt = "{\"" + key + "\":" + value * size + "}"
#    print attempt
    return attempt

def test(attempt):
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = attempt)
    if child.returncode == -11:
        found = True
        print base64.b64encode(attempt)
    	sys.exit(0)

while found==False:
#    test(seg_int())
#    test(seg_string())
    test(seg_array())
#    test(seg_null())
#    test(seg_bool())
    size += 1
    
	
