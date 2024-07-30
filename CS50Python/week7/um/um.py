import re
import sys

def main():
    print(count(input("Text: ")))
    #print(count2(input("Text: ")))

def count2(s):
    s.lower()
    my_list = s.split()
    counter = 0
    for item in my_list:
        if (item[0] == "u") & (item[1] == "m"):
            counter += 1
    return counter

def count(s):

    matches = re.findall(r"(?:^|\W)um(?:$|\W)", s, flags = re.IGNORECASE)
    #print(matches)

    return len(matches)

if __name__ == "__main__":
    main()
