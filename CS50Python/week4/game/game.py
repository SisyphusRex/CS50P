import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            my_number = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if 0 < guess < my_number:
                        print("Too small!")
                    elif guess > my_number:
                        print("Too large!")
                    elif guess == my_number:
                        sys.exit("Just Right!")
                except ValueError:
                    pass

        except ValueError:
            pass
        except EOFError:
            print("Goodbye")

if __name__ == "__main__":
    main()
