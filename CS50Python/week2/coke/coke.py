def insert_money():
    amt_due = 50
    while amt_due > 0:
        is_bad = True
        while is_bad:
            print("Amount Due: {}".format(amt_due))
            inserted = input("Give me money: ")
            is_bad = money_check(inserted)
        amt_due = amt_due - int(inserted)
    return abs(amt_due)

def money_check(coins):
    accepted_coins = ["25", "10", "5"]
    if coins in accepted_coins:
        print("Good money")
        return False
    else:
        print("Not accepted.")
        return True
def main():
    print("Change Owed: {}".format(insert_money()))
if __name__ == "__main__":
    main()




