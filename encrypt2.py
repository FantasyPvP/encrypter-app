import math as maths


def scramble(msg):  # scrambles the text by switching the rows and columns used 
    dimensions = 1 + int(maths.sqrt(len(msg)))
    arr = []
    for x in range(dimensions):
        inner = []
        for y in range(dimensions):
            if dimensions*x+y < len(msg):
                inner.append(msg[dimensions*x+y])
            else:
                inner.append(" ")
                
        arr.append(inner)
        print(inner)
        
    string = ""
    for y in range(dimensions):
        for x in range(dimensions):
            string += arr[x][y]
    return string


