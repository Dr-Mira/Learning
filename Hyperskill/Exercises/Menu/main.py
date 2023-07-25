food = {'pizza': 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
        'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
        'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'}

order = input()

if order in food:
    print(food[order])
else:
    print("Sorry, we don't have it in the menu")
