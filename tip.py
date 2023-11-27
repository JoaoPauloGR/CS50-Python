def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(tip)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    dollars = float(d)
    return dollars


def percent_to_float(p):
    p = p.replace("%","")
    percent = float(p) / 100
    return percent


main()