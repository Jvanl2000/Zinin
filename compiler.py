import sys
import os

def compile(code):
    tokens = []

    list = code.split()
    for token in list:
        if ";" in token:
            tokens.append(token[:-1])
            tokens.append(";")
        else:
            tokens.append(token)

    print(tokens)

if __name__ == "__main__":
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File does not exist!")
        exit()
    else:
        with open(file_path, "r") as f:
            code = f.read()
        compile(code)