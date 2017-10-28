#!/usr/bin/python
from binascii import a2b_hex, b2a_hex

def detect_aes_ecb(line,blocksize):
    block_count = int(len(line)/blocksize)
    for index in range(block_count):
        for next_index in range(index+1,block_count):
            first = line[index*blocksize:(index+1)*blocksize]
            second = line[next_index*blocksize:(next_index+1)*blocksize]
            if first == second:
                return True
    return False

def main():
    with open('08.txt') as f:
        for line in f:
            line = line.strip()
            result = detect_aes_ecb(a2b_hex(line),16)
            if result == True:
                print("Detected ciphertext:\n", line)

if __name__ == "__main__":
    main()