#usr/bin/python
def pad(s,blocksize):
    padding = blocksize - (len(s) % blocksize)
    return s + (chr(padding) * padding).encode('ascii')

def main():
    block_size = 20
    string = b'YELLOW SUBMARINE'
    padded_string = pad(string,block_size)
    print("Unpadded string:", string)
    print("Padded string:", padded_string)

if __name__ == "__main__":
    main()