import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.fullmatch(r"([0-1]?[0-9]):?([0-5][0-9])? (AM|PM){1} to ([0-1]?[0-9]):?([0-5][0-9])? (AM|PM){1}", s)
    if matches:
        my_list = matches.groups()
        new_list = []
        if my_list[2] == "AM":
            new_list.append(int(my_list[0]))
            new_list.append(int(my_list[1]))
        else:
            new_list.append(int(my_list[0]) + 12)
            new_list.append(int(my_list[1]))
        if my_list[5] == "AM":
            new_list.append(int(my_list[3]))
            new_list.append(int(my_list[4]))
        else:
            new_list.append(int(my_list[3]) + 12)
            new_list.append(int(my_list[4]))
        #print(my_list, "/n", new_list)
        return f"{new_list[0]:02}:{new_list[1]:02} to {new_list[2]:02}:{new_list[3]:02}"
    else:
        raise ValueError("incorrect format")




if __name__ == "__main__":
    main()
