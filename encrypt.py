def cipher(msg, key, enc):
    output = []
    msg = msg.rstrip()

    if key == "none":
        key = random.randint(1, len(chars)-1)

    if enc:
        for char in msg:
            idx = chars.index(char)
            idx = cipherincrementer(idx, key, chars)
            ciphered.append(chars[idx])
    else:
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


while True:
    if input("encrypt or decrypt > ") == "encrypt":
        print(cipher(input("enter message to encrypt > "), "none", True))
    else:
        print(cipher(input("enter message to decrypt > "), input("enter decryption key > "), True))