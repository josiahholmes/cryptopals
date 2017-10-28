#!/usr/bin/python
import challenge03

def main():
    with open("04.txt") as f:
        linecount = 0
        for line in f:
            linecount += 1
            key, score, plaintext = challenge03.bestDecryption(line.strip())
            if score > 0.9:
                print("Ciphertext No.", linecount, ":", line)
                print("Key =", key, "Score =", score)
                print("Plaintext =", plaintext)

if __name__ == "__main__":
    main()