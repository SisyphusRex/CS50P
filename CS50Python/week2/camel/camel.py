def convert(token):
    list = []
    for character in token:
        list.append(character)
    length = len(list)
    for i in range(length):
        if list[i].isupper():
            list[i] = list[i].lower()
            list.insert(i, "_")
    my_string = ''.join(list)
    return my_string

def main():
    input1 = input("Give me camel case variable: ")
    print(convert(input1))

if __name__ == "__main__":
    main()

