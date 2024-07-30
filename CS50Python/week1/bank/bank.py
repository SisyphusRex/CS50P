def get_input():
    #get users input, convert to lower case
    input1 = input("Greet me: ")
    input1 = input1.lower()
    input1 = input1.replace(" ", "")
    input1 = input1[:5]
    #print(input1)
    return input1
def test_input(my_input):
    if my_input[0] == "h":
        if my_input == "hello":
            return 0
        else:
            return 20
    else:
        return 100
def main():
    money = test_input(get_input())
    print("{}{}".format("$", money))
main()



