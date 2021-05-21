budget = float(input())
crew = int(input())
price_clothes = float(input())
clothes = price_clothes * crew
sum_decor = budget * 0.1
if crew > 150:
    discount = clothes - (clothes * 0.1)
    total_cost = sum_decor + discount
else:
    clothes = price_clothes * crew
    total_cost = sum_decor + clothes
if total_cost <= budget:
    cost = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {abs(cost):.2f} leva left.")
elif total_cost > budget:
    cost = budget - total_cost
    print("Not enough money!")
    print(f"Wingard needs {abs(cost):.2f} leva more.")
