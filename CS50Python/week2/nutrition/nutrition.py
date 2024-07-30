def main():
    fruit_name = input("Name a fruit: ")
    fruit_name = fruit_name.lower()
    print("Calories: {}".format(calorie_count(fruit_name)))
    quit()
def calorie_count(token):
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    if token in fruits:
        return fruits[token]
    else:
        quit()
if __name__ == "__main__":
    main()
