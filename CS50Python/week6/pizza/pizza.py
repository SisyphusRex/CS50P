import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("incorrect amount of args")
    token = sys.argv[1]
    #print(f"{token}")
    token_list = token.split(".")
    #print(f"{token_list}")
    if len(token_list) != 2:
        sys.exit("no file extension")
    if token_list[1] != "csv":
        sys.exit("not .csv extension")
    organize(token)

def organize(input):
    try:
        with open(input, "r") as file:
            file_content = file.read()
            #print(file_content)
            line_split = file_content.splitlines()
            #print(line_split)
            my_list = []
            counter = 0
            #separated = file_content.split(",")
            #print(file_content)
            #print(separated)
            #print(line_split)
            for line in line_split:
                yeet = line.split(",")
                my_list.append(yeet)
            #print(my_list)
            print(tabulate(my_list, headers = "firstrow", tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File not found")



if __name__ == "__main__":
    main()
