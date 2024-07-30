def main():
    print(f"{get_fract()}")
def get_fract():
    while True:
        try:
            token = input("Fraction: ")
            list = token.split("/")
            my_percent = round((int(list[0]) / int(list[1])) * 100)
            if 1 < my_percent < 99:
                return f"{my_percent}%"
            elif 0 <= my_percent <= 1:
                return "E"
            elif 99 <= my_percent <= 100:
                return "F"
        except ValueError:
            #print("Not a good fraction.")
            pass
        except ZeroDivisionError:
            #print("Cannot divide by zero")
            pass

if __name__=="__main__":
    main()




