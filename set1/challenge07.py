#!/usr/bin/python
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from base64 import b64encode, b64decode

def aes_ecb_decrypt(ct,key,blocksize):
    assert len(ct) % blocksize == 0
    obj = AES.new(key=key,mode=AES.MODE_ECB)
    plaintext = obj.decrypt(ct)
    return plaintext

def main():
    block_size = 16
    key = b'YELLOW SUBMARINE'
    with open('07.txt') as f:
        ciphertext = b64decode(f.read())
    plaintext = aes_ecb_decrypt(ciphertext,key,block_size)
    print(plaintext)

if __name__ == "__main__":
    main()