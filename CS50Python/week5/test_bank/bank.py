
def value(input1):
    #input1 = input("Greet me: ")
    input1 = input1.lower()
    input1 = input1.replace(" ", "")
    input1 = input1[:5]
    if input1[0] == "h":
        if input1 == "hello":
            return 0
        else:
            return 20
    else:
        return 100
def main():
    money = value(input("Give me greeting: "))
    print("{}{}".format("$", money))

if __name__ == "__main__":
    main()
