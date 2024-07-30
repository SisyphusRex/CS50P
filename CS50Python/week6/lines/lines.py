import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("incorrect amount of args")
    token = sys.argv[1]
    print(f"{token}")
    token_list = token.split(".")
    print(f"{token_list}")
    if len(token_list) != 2:
        sys.exit("no file extension")
    if token_list[1] != "py":
        sys.exit("not .py extension")
    print(f"{count_lines(token)}")

def count_lines(input):
    counter = 0
    try:
        with open(input, "r") as file:
            lines_list = file.readlines()
            lines_list2 = [x for x in lines_list if x.strip()]
            lines_list3 = []
            for lines in lines_list2:
                stripped = lines.lstrip()
                lines_list3.append(stripped)
            for lines in lines_list3:
                if lines[0] != "#":
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("no such file")

if __name__ == "__main__":
    main()







