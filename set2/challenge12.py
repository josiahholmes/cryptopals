#!/usr/bin/python
import os
import binascii
import base64
from Crypto.Cipher import AES

key = None

def pad(text,blocksize):
    padding = blocksize - (len(text) % blocksize)
    return text + (chr(padding) * padding).encode('ascii')

def encryption_oracle(txt):
    global key
    if key is None:
        key = os.urandom(16)
    obj, txt = AES.new(key,AES.MODE_ECB), pad(txt,16)
    return binascii.b2a_hex(obj.encrypt(txt))

if __name__ == "__main__":
    YOUR_STRING = b'You are about to witness the strength of street knowledge.'
    UNKNOWN_STRING = base64.b64decode(b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK''')
    text = YOUR_STRING + UNKNOWN_STRING
    ciphertext = encryption_oracle(text)