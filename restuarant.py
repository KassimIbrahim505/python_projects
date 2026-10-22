def make_coffee():
    coffee_bags = int(input('Enter the remaing coffee bag:'))
    chocolate = int(input('Enter the remaing litres of chocolate:'))
    tea_bags = int(input('Enter the remaing tea bags:'))
    sugar = int(input('Amount of kilos of sugar left: '))
    spices = int(input('The amount of spices left:'))

    if tea_bags < 1:
        return 'The are no tea bags to make black tea'
    elif coffee_bags <= 1:
        return 'U should tell the manager to restock more coffee bags'
print(make_coffee())