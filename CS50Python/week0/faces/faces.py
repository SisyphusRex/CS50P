def convert(myinput):
    myinput = myinput.replace(":)", "🙂")
    myinput = myinput.replace(":(", "🙁")
    return myinput
def main():
    name = input("Give me your face! ")
    name = convert(name)
    print(name)
main()
