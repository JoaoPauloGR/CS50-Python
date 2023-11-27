import validators

email_input = input("What's your email address?")
is_valid = validators.email(email_input)

if is_valid:
    print("Valid")
else:
    print("Invalid")