# create item list
item_list = []

# item input
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        # add the item to the list with all upper case letters
        item_list.append(item.upper())

# sort list
item_list.sort()

# auxiliar variable
prev_element = ""

# print quantity and items of the list
for element in item_list:
    if prev_element != element:
        item_qty = item_list.count(element)
        print(f"{item_qty} {element}")
    prev_element = element