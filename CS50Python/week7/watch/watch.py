import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'embed/(\w+?)"', s)
    if matches:
        my_video = matches.group(1)
        #print(my_video)
        return f"https://youtu.be/{my_video}"
    else:
        return None


if __name__ == "__main__":
    main()
