def main():
    tacos = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0.00
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            total = total + tacos[item]
            print("${:.2f}".format(total))
        except EOFError:
            print("\n")
            quit()
        except KeyError:
            pass
if __name__ == "__main__":
    main()
    quit()

