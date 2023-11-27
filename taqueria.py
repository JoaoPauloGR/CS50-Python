# dictionary with item price
price_dic = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_price = 0.0
while True:
    try:
        item = input("Item: ").title()
    except EOFError:
        break
    else:
        if item in price_dic:
            total_price += price_dic[item]
            total_prince = round(total_price, 2)
            print(f"Total: ${total_price}0")
        else:
            pass
