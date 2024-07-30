def main():
    my_date = convert(check_date(get_date()))
    print(f"{my_date[0]}-{int(my_date[1]):02d}-{int(my_date[2]):02d}")
def get_date():
    while True:
        try:
            date = input("Give me date: ")
            if check_date(date):
                return date
        except EOFError:
            print("")
            quit()

def check_date(date):
    x = 1
    date = date.strip()
    month_dict = {}
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    for i in month_list:
        month_dict[i] = x
        x += 1
    if date.find("/") != -1:
        my_list = date.split("/")
        #print(my_list)
        return my_list
    else:
        date = date.replace(",", "")
        my_list = date.split()
        #print(my_list)
        if my_list[0] in month_dict:
            hold_list = ["month", "day", "year"]
            hold_list[0] = month_dict[my_list[0]]
            hold_list[1] = my_list[1]
            hold_list[2] = my_list[2]
            #print(hold_list)
            return hold_list
        else:
            return False
def convert(my_list):
    #print(my_list)
    new_list = ["month", "day", "year"]
    new_list[0] = my_list[2]
    new_list[1] = my_list[0]
    new_list[2] = my_list[1]
    #print(f"converted: {new_list}")
    return new_list
if __name__ == "__main__":
    main()





