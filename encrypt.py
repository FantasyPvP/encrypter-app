def cipher(msg):
    ciphered = []
    msg = msg.rstrip()
    key = random.randint(1, len(chars)-1)
    for char in msg:
        idx = chars.index(char)
        #print(idx, char, "enc1")
        idx += key

        if idx >= len(chars):
            idx -= len(chars)
        #print(idx, chars[idx], "enc2")
        ciphered.append(chars[idx])
    
    #print("CIPHERED:", "".join(ciphered))
    result = "".join(ciphered)

    return (result.rstrip(), key)
    
def decipher(msg, key):
    deciphered = []
    for char in msg:
        idx = chars.index(char)
        #print(idx, char, "dec1")
        idx -= key

        if idx < 0:
            idx += len(chars)

        #print(idx, chars[idx], "dec2")
        deciphered.append(chars[idx])

    result = "".join(deciphered)
    return result

def cipherincrementer(idx, key, chars):
    idx += key

    if idx >= len(chars):
        idx -= len(chars)


def cipherdecrementer(idx, key, chars):
    idx -= key

    if idx < 0:
        idx += len(chars)