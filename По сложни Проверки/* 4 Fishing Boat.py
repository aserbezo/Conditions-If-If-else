budget = int(input())
season = input()
fishermen = int(input())
discount = 1.00
price = 0.00
if season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Spring':
    price = 3000
elif season == 'Winter':
    price = 2600
if fishermen <= 6:
    price *= 0.9
elif fishermen <= 11:
    price *= 0.85
else:
    price *= 0.75

if season != 'Autumn' and fishermen % 2 == 0:
    price *= 0.95

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')