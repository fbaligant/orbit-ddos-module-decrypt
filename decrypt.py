# Orbit Downloader Memory Module PE Payload
# Configuration file decryption
# aXs^http://codezen.fr
#
# PE MD5: 809D5A4AF232F08F88D315B116E47828
#
# You need Python Request - http://www.python-requests.org/

import requests
from urllib import unquote
from base64 import b64decode
from hashlib import md5

r = requests.get('http://obupdate.orbitdownloader.com/update/il.php')

key = md5('A!)$>da*b').hexdigest()

print "key=", key

cipher = b64decode(r.text)

step1 = ''

k = 0
for c in cipher:
    step1 += chr(ord(c) ^ ord(key[k % len((key))]))
    k += 1

step2 = ''
for (c1, c2) in zip(step1[0::2], step1[1::2]):
    step2 += chr(ord(c1) ^ ord(c2))

print unquote(step2)