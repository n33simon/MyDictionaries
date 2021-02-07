dictionary = {}


def main():
    with open("text.txt") as file_object:
        contents = file_object.read()
        words = contents.split()
        num_words = len(words)

    for word in words[:]:
        if word not in dictionary:
            dictionary[word] = words.count(word)
        # total = dictionary.get(word, "")

    print(dictionary)
    return dictionary


main()

# the instructions did not ask for the words recorded with or without capitalizing difference so I did not add it in
