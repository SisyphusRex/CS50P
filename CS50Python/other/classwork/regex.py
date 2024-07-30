import re
import sys

#i did not understand why the ^ and $ match symbols made the
#email example in the video fail.  the email fails not because of
#spaces in the first half of the email, but the period at the end
#if input equals: "this is my email malan@harvard.edu."
#the final period fails the email, not the spaces before the @
#which are just chars in a string
def main():
    try:
        email = input("What's your email? ").strip()
        if re.search(r"^.+", email):
            print("passed carrot in beginning")
        if re.search(r".+\.edu$", email):
            print("passed $ at end")
        if re.search(r"^.+@.+\.edu$", email):
            print("Valid")
        else:
            print("Invalid")
    except EOFError:
        sys.exit("\ngoodbye")

if __name__ == "__main__":
    main()
