import random


def main():
    score = 0
    level_num = get_level()
    for i in range(10):
        chances = 3
        x, y = generate_integer(level_num)
        str_expression = (str(x) + " + " + str(y) + " = ")
        while True:
            answer = int(input(str_expression))
            if answer == (x + y):
                score += 1
                break
            else:
                chances -= 1
                if chances != 0:
                    print("EEE")
                else:
                    print(str_expression + str(x + y))
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level_num = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level_num not in [1,2,3]:
                pass
            else:
                return level_num


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y

if __name__ == "__main__":
    main()