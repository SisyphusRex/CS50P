def check_user_input(input):
    try:
        val = int(input)
        print("You provided an integer.")
        return True
    except ValueError:
        print("Not an integer.")
        return False
def get_input():
    x = False
    while x == 0:
        user_in = input("Give me an integer: ")
        x = check_user_input(user_in)
    return user_in
def formula(mass_in):
    y = int(mass_in)
    x = y * 90000000000000000
    return x
def main():
    x = get_input()
    y = formula(x)
    print(y)
main()








