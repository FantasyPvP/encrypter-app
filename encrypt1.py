import random

global chars
chars  = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x","y","z"
]

def cipher(msg, key, enc):

    other = None

    output = []
    msg = msg.lower().rstrip()

    if key == "none":
        key = random.randint(1, len(chars)-1)


    if enc:
        try:
            key = int(key)
        except:
            other = "invalid key, generated new one"
            key = random.randint(1, len(chars)-1)

        for char in msg:
            if char != " ":
                idx = chars.index(char)
                idx = cipherincrementer(idx, key, chars)
                output.append(chars[idx])
            else:
                output.append(char)
    else:

        try:
            key = int(key)
        except ValueError:
            other = "Invalid key"
            return("err", None, key, other)

        for char in msg:
            if char != " ":
                idx = chars.index(char)
                idx = cipherdecrementer(idx, key, chars)
                output.append(chars[idx])
            else:
                output.append(char)

    result = "".join(output)

    return ("ok", result.rstrip(), key, other)


def cipherincrementer(idx, key, chars):
    idx += key

    while idx >= len(chars):
        idx -= len(chars)
    return idx

def cipherdecrementer(idx, key, chars):
    idx -= key
    while idx < 0:
        idx += len(chars)
    return idx


if __name__ == "__main__":
    while True:
        if input("encrypt or decrypt > ") == "encrypt":
            print(cipher(input("enter message to encrypt > "), "none", True))
        else:
            print(cipher(input("enter message to decrypt > "), int(input("enter decryption key > ")), False))
