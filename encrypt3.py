import random
from encrypt import chars


def encrypt(msg):
    randomstring = ""
    randomstring += "".join([random.choice(chars) for i in range(len(msg))])

    return xor(msg, randomstring), randomstring


def decrypt(msg, key):
    return xor(msg, key)



def xor(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])

    return ''.join(xored)
    









if __name__ == "__main__":
    encrypt("L")
