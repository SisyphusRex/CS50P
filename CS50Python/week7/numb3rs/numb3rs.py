import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
    #print(validate2(input("IPv4 Address: ")))

def validate2(ip):
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        return False
    my_list = list(range(0, 256))
    #print(my_list)
    #print(ip_list)
    for item in ip_list:
        if int(item) not in my_list:
            #print(item)
            return False
    return True

def validate(ip):
    matches = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
    if matches:
        ip_list = matches.groups()
        my_list = list(range(0, 256))
        for item in ip_list:
            if int(item) not in my_list:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
