import base64



def encrypt(msg):
    return base64.b64encode(msg)

def decrypt(msg):
    return base64.b64decode(msg)













if __name__ == "__main__":
    encrypt("L")
