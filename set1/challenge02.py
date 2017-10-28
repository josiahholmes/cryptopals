#!/usr/bin/python
def hexxor(str1, str2):
    hexxor = ''
    assert len(str1) == len(str2)
    hexxor = int(str1,16) ^ int(str2,16)
    return '{:x}'.format(hexxor)

def main():
    string1 = '1c0111001f010100061a024b53535009181c'
    string2 = '686974207468652062756c6c277320657965'
    result = hexxor(string1,string2)

    print("String 1 =", string1)
    print("String 2 =", string2)
    print("Fixed XOR =", result)

if __name__ == "__main__":
    main()