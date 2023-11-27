def main():
    time_var = input("What time is it? ")
    time_convert = convert(time_var)
    if 7 <= time_convert <=8:
        print("breakfast time")
    elif 12 <= time_convert <= 13:
        print("lunch time")
    elif 18 <= time_convert <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    minute = int(minute)/60
    final_time = float(hour) + minute

    return final_time

if __name__ == "__main__":
    main()