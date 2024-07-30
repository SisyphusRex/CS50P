def main():
    initial = input("Give me word: ")
    initial = shorten(initial)
    print(initial)

def shorten(my_word):
    list1 = []
    list2 = []
    for character in my_word:
        list1.append(character)
    banned_vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for object in list1:
        if object not in banned_vowels:
            list2.append(object)
    my_string = ''.join(list2)
    return my_string


if __name__ == "__main__":
    main()
