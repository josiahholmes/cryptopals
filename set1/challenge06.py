#!/usr/bin/python
import challenge3
from binascii import b2a_hex, a2b_hex
from base64 import b64encode, b64decode

def getHamDist(string1,string2):
    assert len(string1) == len(string2)
    string1 = ' '.join(bin(letter)[2:].zfill(8) for letter in string1)
    string2 = ' '.join(bin(letter)[2:].zfill(8) for letter in string2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(string1,string2))

def getKeySize(ciphertext):
    bestKey = 9999
    bestScore = 9999
    for keysize in range(2,41):
        str1 = ciphertext[0:14*keysize]
        str2 = ciphertext[14*keysize:2*14*keysize]
        hamdist = getHamDist(str1,str2)
        score = (float(hamdist) / (14*keysize))

        if(score < bestScore):
            bestKey, bestScore = keysize, score

    print("The probable keysize is", bestKey, "with a hamming distance of", bestScore)
    return bestKey

def findRepeatingKey(ciphertext,keysize):
    j = 0
    key = ''
    testcipher = ''
    transposed = []
    transHexLen = int((keysize/2) + 1)
    ciphertext = [ciphertext[i:i+keysize*2] for i in range(0,len(ciphertext),keysize)]

    for ctblock in ciphertext:
        ctblock = [ctblock[i:i+2] for i in range(0,len(ctblock),2)]
        transposed.append(ctblock)

    for ctblock in transposed:
        if len(ctblock) != transHexLen:
            del transposed[-1]

    for j in range(keysize):
        for ctblock in transposed:
            testcipher += str(ctblock[j]).strip('b').strip('\'')
        keyChar, score, plaintext = challenge3.bestDecryption(testcipher)
        if len(key) < keysize:
            key += chr(keyChar)
            testcipher = ''
    if len(key) == keysize:
        print("Key found! Key is:", key)
    return key

def repeatingKeyXOR(ciphertext,key):
    k, result = list(key), ''
    ciphertext = [ciphertext[i:i+2] for i in range(0,len(ciphertext),2)]
    for i in range(len(ciphertext)):
        plaintext = chr(int(ciphertext[i],16) ^ ord(k[i%len(k)]))
        result += plaintext
    print("The plaintext is:")
    print(result)

def main():
    with open('06.txt') as f:
        ciphertext = (b2a_hex(b64decode(f.read())))
    keysize = getKeySize(ciphertext)
    key = findRepeatingKey(ciphertext,keysize)
    repeatingKeyXOR(ciphertext,key)

if __name__ == "__main__":
    main()