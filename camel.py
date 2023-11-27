def snake(str_input):
    if str_input.islower():
        str_output = str_input
    else:
        list_output = []
        for i in range(len(str_input)):
            letter = str_input[i]
            if letter.isupper():
                list_output.append("_")
                list_output.append(letter.lower())
            else:
                list_output.append(letter)
            str_output = "".join(list_output)
    return str_output

# camel case input
camel_input = input("camelCase: ")
snake_output = snake(camel_input)

print(snake_output)
