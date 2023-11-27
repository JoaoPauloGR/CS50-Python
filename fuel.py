while True:
    # asks expression for the user
    expression_str = input ("Fraction: ")
    try:
        x, y = expression_str.split("/")
    except ValueError:
        pass
    else:
        try:
            division = int(x)/int(y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if division > 1:
                pass
            else:
                break

if division >= 0.99:
    print("F")
elif division <= 0.01:
    print("E")
else:
    div_rounded = round(division * 100)
    print(f"{div_rounded}%")
