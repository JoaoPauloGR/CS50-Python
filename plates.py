def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check plate length
    if len(s) > 6 or len(s) < 2:
        return False
    # check if everything is alphanumeric - no punctuation or symbols
    elif not s.isalnum():
        return False
    # check if the first two characters are letters
    elif not s[0:2].isalpha():
        return False
    else:
        first_number = ""
        for i in range(len(s)):
            # the first number cannot be zero
            if s[i].isnumeric() and first_number == "":
                if s[i] == "0":
                    return False
                else:
                    first_number = s[i]
            # check if there is not numbers in the middle of the string
            elif s[i].isnumeric() and (not s[-1].isnumeric() or not s[-2].isnumeric()):
                return False
        else:
            return True

if __name__ == "__main__":
    main()