import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search("(\d+)(?::(\d{2}))? ([AP]+M) to (\d+)(?::(\d{2}))? ([AP]+M)", s):
        start = matches.group(1)
        start_min = matches.group(2)
        end = matches.group(4)
        end_min = matches.group(5)

        # treatment for pm hours
        if matches.group(3) == "PM":
            start = int(matches.group(1)) + 12
            if start == 24:
                start = 12
        elif matches.group(3) == "AM" and int(matches.group(1)) == 12:
            start = 0
        else:
            start = int(matches.group(1))

        if matches.group(6) == "PM":
            end = int(matches.group(4)) + 12
            if end == 24:
                end = 12
        elif matches.group(6) == "AM" and int(matches.group(4)) == 12:
            end = 0
        else:
            end = int(matches.group(4))

        # treatment if minutes are missing
        if start_min == None:
            start_min = "00"
        elif int(start_min) >= 60:
            raise ValueError

        if end_min == None:
            end_min = "00"
        elif int(end_min) >= 60:
            raise ValueError

        return f"{start:02}:{start_min} to {end:02}:{end_min}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()