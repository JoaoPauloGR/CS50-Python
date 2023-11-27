def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.strip().lower().startswith("hello"):
        greeting_val = 0
    elif greeting.strip().lower().startswith("h"):
        greeting_val = 20
    else:
        greeting_val = 100

    return greeting_val

if __name__ == "__main__":
    main()