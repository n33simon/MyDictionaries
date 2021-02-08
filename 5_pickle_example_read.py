import pickle

infile = open("names_pickle_file_write.dat", "rb")  # rb b/c its binary--> read binary

names = pickle.load(infile)

print(type(names))

print(names)

name = input("Add a name to the list: ")
names.append(name)

# the ^name^ would be added to the list in terminal but NOT in the pickle file
# (we didn't dump it again)
print(names)

# here's the update (below) that would dump the update to the pickle file
pickle.dump("names_pickle_file_write.dat", "wb")
pickle.dump(names, outfile)


# pickle works w/ ANY python object
