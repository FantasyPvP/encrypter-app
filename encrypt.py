import random

global chars
chars  = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
    "T","U","V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9","0",
    " ", "\"", "\\","!","'","$","%","^","&","*","(",")",
    "[","]","<",">","{","}",":",
    "|","/","@",";","~","#","-","_","=","+","`", ",", ".", "?", "£"
]

def cipher(msg, key, enc):

    print(msg, key, enc)

    output = []
    msg = msg.rstrip()

    if key == "none":
        key = random.randint(1, len(chars)-1)

    if enc == "1":
        print("a")
        for char in msg:
            idx = chars.index(char)
            idx = cipherincrementer(idx, key, chars)
            output.append(chars[idx])
    else:
        print("b")
        for char in msg:
            idx = chars.index(char)
            idx = cipherdecrementer(idx, key, chars)
            output.append(chars[idx])

    result = "".join(output)

    return (result.rstrip(), key)
    

def cipherincrementer(idx, key, chars):
    idx += key

    if idx >= len(chars):
        idx -= len(chars)
    return idx

def cipherdecrementer(idx, key, chars):
    idx -= key
    if idx < 0:
        idx += len(chars)
    return idx


if __name__ == "__main__":
    while True:
        if input("encrypt or decrypt > ") == "encrypt":
            print(cipher(input("enter message to encrypt > "), "none", True))
        else:
            print(cipher(input("enter message to decrypt > "), int(input("enter decryption key > ")), False))