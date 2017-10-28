#!/usr/bin/python
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64decode
from binascii import unhexlify, hexlify

class CBC:
    def __init__(self,mode,ciphertext):
        self.CBC = mode
        self.ciphertext = ciphertext
        self.plaintext = self.aes_cbc_decrypt(self.CBC,self.ciphertext)

    def aes_cbc_decrypt(self,mode,ciphertext):
        return mode.decrypt(ciphertext)

    def __str__(self):
        return str(self.plaintext)

if __name__ == "__main__":
    f = open('10.txt')
    ciphertext = b64decode(f.read().strip('\n'))
    f.close()

    iv = b'\x00'*16
    key = b'YELLOW SUBMARINE'

    plaintext = CBC(AES.new(key,AES.MODE_CBC,iv),ciphertext)
    print(plaintext)