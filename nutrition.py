# dictionary with fruits and calories
fruits_calories = {"apple":"130", "avocado":"50", "banana":"110","cantaloupe":"50", "grapefruit":"60","grapes":"90",
                   "honeydew melon":"50", "kiwifruit":"90", "lemon":"15", "nectarine":"60", "orange":"80", "peach":"60",
                   "pear":"100", "pineapple":"50", "plums":"70", "strawberries":"50", "sweet cherries":"100",
                   "tangerine":"50", "watermelon":"80"}

fruit_keys = fruits_calories.keys()
print(fruit_keys)
chosen_fruit = input("Item: ")
if chosen_fruit.lower() in fruit_keys:
    print("Calories:",fruits_calories[chosen_fruit.lower()])
