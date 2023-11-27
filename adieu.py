import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        name_input = input("Name: ")
    except EOFError:
        break
    else:
        names_list.append(name_input)

names_str = p.join(names_list)


print("Adieu, adieu, to " + names_str)