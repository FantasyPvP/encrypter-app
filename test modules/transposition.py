import math
# know that this algorithm works reliably because ive used and tested it before in this exact form

def main(msg):
    dimensions = 1 + int(math.sqrt(len(msg)))
    arr = []
    for x in range(dimensions):
        inner = []
        for y in range(dimensions):
            if dimensions*x+y < len(msg):
                inner.append(msg[dimensions*x+y])
            else:
                inner.append(" ")

        arr.append(inner)

    string = ""
    for y in range(dimensions):
        for x in range(dimensions):
            string += arr[x][y]
    return string

print(main(input("enter message > ")))
