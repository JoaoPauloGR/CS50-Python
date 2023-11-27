# input of coins
coins = [5, 10,25]
coin_inserted = 0
total_value = 0
original_price = 50
amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted in coins:
        amount_due = amount_due - coin_inserted
        total_value = total_value + coin_inserted

print("Change Owed:", total_value - original_price)