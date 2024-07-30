def main():
    groceries = {}
    while True:
        try:
            item = input().lower()
            if item in groceries:
                groceries[item] = groceries[item] + 1
            else:
                groceries[item] = 1
        except KeyError:
            pass
        except EOFError:
            print("")
            x = sort_dict(groceries)
            for i in x:
                print(f"{x[i]} {i.upper()}")
            quit()
def sort_dict(dicts):
    key_list = sorted(dicts)
    sorted_dict = {}
    for i in key_list:
        sorted_dict[i] = dicts[i]
    return sorted_dict

if __name__ == "__main__":
    main()

