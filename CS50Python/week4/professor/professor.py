import random


def main():
    level = get_level()
    my_range = range(10)
    correct = 0
    for n in my_range:
        x = generate_integer(level)
        y = generate_integer(level)
        my_sum = x + y

        counter = 0
        sub_range = range(3)
        for m in sub_range:
            try:
                user_answer = input(f"{x} + {y} = ")
                if int(user_answer) == my_sum:
                    correct += 1
                    break
                elif counter == 2:
                    print(f"{x} + {y} = {my_sum}")
                    break
                else:
                    print("EEE")
                    counter += 1
            except ValueError:
                if counter == 2:
                    print(f"{x} + {y} = {my_sum}")
                    break
                else:
                    print("EEE")
                    counter += 1
                pass
    print(f"Score: {correct}")




def get_level():
    level_list = [1, 2, 3]
    while True:
        level = int(input("Level: "))
        if level in level_list:
            return level
        else:
            raise ValueError




def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)




if __name__ == "__main__":
    main()
