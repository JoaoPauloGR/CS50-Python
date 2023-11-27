def main():
    while True:
        # asks expression for the user
        fraction = input ("Fraction: ")
        if "/" not in fraction:
            pass
        else:
            percentage = convert(fraction)
            fuel_gauge = gauge(percentage)
            print(fuel_gauge)


def convert(fraction):
        x, y = fraction.split("/")
        try:
            division = int(x)/int(y)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            if division > 1:
                raise ValueError("There is more fuel than expected")
            else:
                return int(division * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 0.01:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()