import inflect
p = inflect.engine()

def main():
    my_list = []
    try:
        while True:
            #get input of names
            my_input = input("Name: ")
            my_list.append(my_input)

    except EOFError:
        #format and bid adieu to the names
        my_list = p.join(my_list)
        #print(my_list)
        print(f"Adieu, adieu, to {my_list}")

if __name__ == "__main__":
    main()

