from validator_collection import validators, checkers, errors

def main():
    print(validate(input("Email: ")))

def validate(s):
    #checkers.is_email(value) checks the value for email and returns true or false
    yeet = checkers.is_email(s)
    if yeet:
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()
