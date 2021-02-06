dictionary = {}


def main():
    text_file()


def text_file():
    with open("text.txt") as file_object:
        contents = file_object.read()
        words = contents.split()
        num_words = len(words)

    for word in words[:]:
        if word not in dictionary:
            dictionary[word] = words.count(word)
        total = dictionary.get(word, "")

    print(dictionary)
    return dictionary


main()