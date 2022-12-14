from encrypt1 import chars
import random


def process(text):

    # atbash cipher
    rev = list(reversed(chars))

    result = ""

    for char in text:
        if not char in chars and not char == " ":
            return ("err", None, None, "invalid character")


    for char in text:
        if char != " ":
            idx = chars.index(char)
            newchar = rev[idx]
            result += newchar

        else:
            result += " "

    return ("ok", result, None, None)
