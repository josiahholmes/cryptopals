#!/usr/bin/python
from binascii import a2b_hex
from base64 import b64encode

def hexToBase64(text):
    hexct = a2b_hex(text)
    b64ct = b64encode(hexct)
    return b64ct

def main():
    ciphertext = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64cipher = hexToBase64(ciphertext)

    print("hexCipher =", ciphertext)
    print("b64Cipher =", b64cipher)

if __name__ == "__main__":
    main()