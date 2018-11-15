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
#        print attempt
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
        for i in range (random.randint(1, size)): 
                value.append(random.choice(pchar))

        tmp = {key : value}
        attempt = json.dumps(tmp)
#        print attempt
        return attempt
 
def seg_object():

        key0 = ''.join(random.choice(letters))
        key1 = ''.join(random.choice(letters))
        key2 = ''.join(random.choice(letters))
        key3 = ''.join(random.choice(letters))
        key4 = ''.join(random.choice(letters))
        value0 = ''.join((random.choice(pchar) for i in range (random.randint(0, size))))
        value0 = value0 * size
        value1 = ''.join((random.choice(nums) for i in range (random.randint(0, size))))
        value1 = value1 * size
        value2 = []
        for i in range (random.randint(1, size)):
                value2.append(random.choice(pchar))
        value3 = ''.join((random.choice(p_bool) for i in range(random.randint(1, size))))
        value3 = value3 * size
        value4 = ''.join(('\x00' for i in range (random.randint(0, size))))
        value4 = value4 * size
        
        tmp = {
                key0 : value0,
                key1 : value1,
                key2 : value2,
                key3 : value3,
                key4 : value4              
        }
        attempt = json.dumps(tmp)

        print attempt
        return attempt
        
def seg_bool():
        # Flipping a coin 5 times would give you a 96% confidence interval you would get one of either heads or tails
        key = ''.join(random.choice(letters))
        value = ''.join((random.choice(p_bool) for i in range(random.randint(1, size))))
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
#        test(seg_int())
#        test(seg_string())
#        test(seg_array())
        test(seg_object())
#        test(seg_null())
#        test(seg_bool())
        size += 1
        
                
