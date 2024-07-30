def convert(my_string):
    list = my_string.split(':')
    hour = int(list[0])
    minute = float(list[1])
    minute = minute / 60
    hours = hour + minute
    #print(hours)
    return hours
def check(my_time):
    if 7 <= my_time <= 8:
        return "breakfast time"
    elif 12 <= my_time <= 13:
        return "lunch time"
    elif 18 <= my_time <= 19:
        return "dinner time"
    else:
        return False
def main():
    token = input("What time is it? ")
    token = convert(token)
    my_result = check(token)
    if my_result != False:
        print(my_result)
if __name__ == "__main__":
    main()


