#!/usr/bin/python
import os
from Crypto import Random
from Crypto.Cipher import AES
from random import randrange, randint
from base64 import b64decode, b64encode
from binascii import unhexlify, hexlify

def main():
    def pad(s, size):
        return (size * '{') + s + (size * '{')

    def unpad(s):
        l = s.count('{')
        return s[(l/2):len(s)-(l/2)]

    def randnum():
        return randrange(0,2,1)

    def randpadsize():
        return randint(5,10)

    def randkey(block_size):
        return hexlify(Random.new().read(block_size))

    def encrypt_ECB(plaintext,key):
        obj = AES.new(key,AES.MODE_ECB)
        ciphertext = obj.encrypt(plaintext)
        return ciphertext

    def decrypt_ECB(ciphertext,key):
        obj = AES.new(key,AES.MODE_ECB)
        plaintext = obj.decrypt(ciphertext)
        return plaintext

    def encrypt_CBC(plaintext,key,iv):
    	obj = AES.new(key,AES.MODE_CBC,iv)
        ciphertext = obj.encrypt(plaintext)
        return ciphertext

    def decrypt_CBC(ciphertext,key,iv):
        obj = AES.new(key,AES.MODE_CBC,iv)
        plaintext = obj.decrypt(ciphertext)
        return plaintext

    def encryption_oracle(plaintext):
        padding_size = randpadsize()
        plaintext = pad(plaintext,padding_size)
        block_count = len(plaintext)/16
        ciphertext = ''
        for i in range(block_count):
            ptblock = plaintext[i*16:(i+1)*16]
            num = randnum()
            key = randkey(16)
            if num is 0:
                encrypted_ptblock = encrypt_ECB(ptblock,key)
                print "Plaintext block encrypted in ECB mode . . . "
            if num is 1:
                iv = os.urandom(16)
                encrypted_ptblock = encrypt_CBC(ptblock,key,iv)
                print "Plaintext block encrypted in CBC mode . . . "
            ciphertext += encrypted_ptblock
        return ciphertext

if __name__ == "__main__":
    f = open('blueswede.txt', 'r+')
    plaintext = f.read().strip('\n')
    f.close()

    ciphertext = encryption_oracle(plaintext)

    g = open('hoaf.txt', 'w+')
    g.write(b64encode(ciphertext))
    g.close()