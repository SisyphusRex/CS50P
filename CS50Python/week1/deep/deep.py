def get_input():
    #get users input, convert to lower case
    input1 = input("What is the Great Question of Life? ")
    input1 = input1.lower()
    input1 = input1.replace(" ", "")
    return input1
def test_input(my_string):
    #test input against key
    match my_string:
        case "42":
            return True
        case "fortytwo":
            return True
        case "forty-two":
            return True
        case _:
            return False
def main():
    if test_input(get_input()):
        print("Yes\n")
    else:
        print("No\n")
main()



