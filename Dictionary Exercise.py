filename = "text.txt"

try:
    with open(filename) as f:
        contents = f.read()
        print(contents)
 