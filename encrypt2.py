import random
import string

def main():
    print(enc(input("encrypt or unencrypt? [D/E] > "), input("enter string to process > "), getkey()))

def getkey():
    key = "".join(random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(16))
    print(key)
    return key

def enc(opt, msg, key):
    print("bruh", key)
    match opt:
        case "D":
            key = input("enter key > ")
            idx = 0
            new = ""
            for char in msg:
                print("lol", ord(char))
                new += chr(ord(char) - ord(key[idx]))
                idx += 1
                if idx >= len(key):
                    idx = 0
        case "E":
            idx = 0
            new = ""
            for char in msg:
                new += chr(ord(char) + ord(key[idx]))
                idx += 1
                if idx >= len(key):
                    idx = 0
        case _:
            raise Exception("invalid option")
    return (new, key)









main()
