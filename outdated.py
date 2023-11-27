# month list
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Date: ")
    # checks for date input type
    if "/" in date_input:
        m, d, y = date_input.split("/")
        try:
            m = int(m)
        except ValueError:
            pass
        else:
            y = y.strip()
            d = int(d)
            if m > 12 or d > 31:
                pass
            else:
                break
    elif "," in date_input:
        m, d, y = date_input.split(" ")
        try:
            m = month_list.index(m)
        except ValueError:
            pass
        else:
            m = int(m) + 1
            d = int(d.replace(",",""))
            if m > 12 or d > 31:
                pass
            else:
                break
    else:
        pass

# formats for day, month and year
print(f"{y}-{m:02}-{d:02}")