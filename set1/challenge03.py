#!/usr/bin/python
def bestDecryption(ciphertext):
    bestKey = -1
    maxScore = -1
    bestPlaintext = ''
    for val in range(256):
        plaintext = xorDecrypt(ciphertext,val)
        score = englishScore(plaintext)

        if score > maxScore:
            maxScore, bestKey, bestPlaintext = score, val, plaintext

    return (bestKey, maxScore, bestPlaintext)

def xorDecrypt(ciphertext,val):
    cipherBlocks = [ciphertext[i:i+2] for i in range(0,len(ciphertext),2)]
    phrase = ''
    for b in cipherBlocks:
        phrase += chr(int(b,16) ^ val)
    return phrase

def englishScore(plaintext):
    score = 0
    for letter in plaintext:
        if letter in ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            score += 1
    return float(score)/len(plaintext)

def main():
    ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    key, score, plaintext = bestDecryption(ciphertext)

    print("Ciphertext =", ciphertext)
    print("Challenge 3 Answer:")
    print("Key =", key, "Score =", score)
    print("Plaintext =", plaintext)

if __name__ == "__main__":
    main()