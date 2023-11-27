from datetime import date
import inflect
import sys

def main():
    date_input = input("Date of Birth: ")
    # convert string to date object
    birth_date = convert_date(date_input)
    # today's date
    today = date.today()
    num_minutes = (today - birth_date).days * 24 * 60
    minutes_str = number_to_str(num_minutes)
    print(f"{minutes_str.capitalize()} minutes")

def convert_date(date_input):
    try:
        year, month, day = date_input.split("-")
    except ValueError:
        sys.exit("Invalid Date")
    else:
        return date(int(year), int(month), int(day))

def number_to_str(num_min):
    p = inflect.engine()
    return p.number_to_words(num_min, andword = "")

if __name__ == "__main__":
    main()