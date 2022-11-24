import random

def main():
    x = input("encrypt or decrypt [D/E] > ")
    if x == "E":
        out = enc2(input("enter text to encrypt > "))
    elif x == "D":
        out = dec2(input("enter text to decrypt > "))
    else:
        raise Exception("invalid input must be [D/E]")

    print(out)


def enc2(txt):
    new = ""
    for idx, char in enumerate(txt):
        new += f"{char}{txt[len(txt) - idx - 1]}"
    return new

def dec2(txt):
    print(txt)
    new = ""
    original = True

    for char in txt:
        if original:
            new += char
            original = False
        else:
            original = True

    return new

main()