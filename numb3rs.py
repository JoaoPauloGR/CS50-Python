import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for i in range (len(matches.groups())):
            if int(matches.group(i+1)) > 255:
                return False
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()