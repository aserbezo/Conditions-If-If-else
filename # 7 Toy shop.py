# Да се напише програма, която пресмята печалбата от поръчката.
# Цени на играчките:
# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# От конзолата се четат 6 реда:

price_of_the_excursion = float(input())
puzzle = int(input())
talking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
sum_all = puzzle * 2.60 + talking_dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
toys = puzzle + talking_dolls + bears + minions + trucks
if toys >= 50:
    sum_all = sum_all - sum_all * 0.25
rent = sum_all * 0.1
sum_all = sum_all - rent
if sum_all >= price_of_the_excursion:
    profit = sum_all - price_of_the_excursion
    print(f"Yes! {abs(profit):.2f} lv left.")
else:
    profit = price_of_the_excursion - sum_all
    print(f"Not enough money! {abs(profit):.2f} lv needed.")


# 320
# 8
# 2
# 5
# 5
# 1
# Not enough money! 238.73 lv needed.


# 40.8
# 20
# 25
# 30
# 50
# 10
# Yes! 418.20 lv left.