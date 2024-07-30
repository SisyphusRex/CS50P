def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    my_list = make_list(s)
    if two_letters(my_list) and length_check(my_list) and numbers_check(my_list) and character_check(my_list):
        return True
    else:
        return False
def make_list(token):
    list = []
    for character in token:
        list.append(character)
    #print(list)
    return list
def two_letters(token):
    if len(token) < 2:
        return False
    if token[0].isalpha() and token[1].isalpha():
        #print("two_letters True")
        return True
    else:
        #print("two_letters False")
        return False
def length_check(token):
    if len(token) > 6:
        #print("length_check False")
        return False
    else:
        #print("length_check True")
        return True
def numbers_check(token):
    length = len(token)
    #print(length)
    num_counter = 0
    for i in range(length):
        if token[i].isnumeric():
            if (token[i] == "0") and num_counter == 0:
                #print("first number 0")
                return False
            num_counter += 1
        if token[i].isalpha() and (num_counter != 0):
            #print("alpha after number")
            return False
    return True
def character_check(token):
    for character in token:
        if not(character.isalpha() | character.isnumeric()):
            return False
    return True
if __name__ == "__main__":
    main()





