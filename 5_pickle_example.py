# Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled
# so that it can be saved on disk. What pickle does is that it “serializes” the object first before writing it to file.
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character
# stream contains all the information necessary to reconstruct the object in another python script.

import pickle
import os

path = "names_pickle_file.dat"

# outfile = open("names_pickle_file.dat", "ab")
# first time you run it keep this line^^ uncommented so you create the initial path

print(os.path.getsize(path))


if os.path.getsize(path) > 0:
    infile = open("names_pickle_file.dat", "rb")
    names = pickle.load(infile)
    name = input("Add a name to the list: ")
    names.append(name)
else:
    names = []
    name = input("Add a name to the list: ")
    names.append(name)

# first time you run it keep the below line commented out
outfile = open("names_pickle_file.dat", "ab")
pickle.dump(names, outfile)
outfile.close()

print(names)


# ISSUE: DOES NOT ADD THE NAME TO THE END OF LIST BUT INCREASES PATH SIZE
