#!/usr/bin/python
def repeatingKeyXOR(plaintext,key):
    pt, k, result = list(plaintext), list(key), ''
    for i in range(len(pt)):
        cipher = chr(ord(pt[i]) ^ ord(k[i%len(k)]))
        result += hex(ord(cipher))[2:]
    return result

def main():
    key = "ICE"
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ciphertext = repeatingKeyXOR(plaintext,key)

    print("Plaintext =", plaintext)
    print("Key =", key)
    print("Ciphertext =", ciphertext)

if __name__ == "__main__":
    main()