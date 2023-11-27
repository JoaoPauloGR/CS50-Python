def main():
    word = input("Input: ")
    str_output = shorten(word)
    print("Output:", str_output)


def shorten(word):
    list_output = []
    vowels = ["a","e","i","o","u"]
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            list_output.append(word[i])

    str_output = "".join(list_output)

    return str_output

if __name__ == "__main__":
    main()