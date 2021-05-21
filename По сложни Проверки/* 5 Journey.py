budget = float(input())
season = input()
amount_spent = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
       amount_spent = budget * 0.3
       type = "Camp"
    else:
        season == "winter"
        amount_spent = budget * 0.7
        type = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        amount_spent = budget * 0.4
        type = "Camp"
    else:
        season == "winter"
        amount_spent = budget * 0.8
        type = "Hotel"
else:
    destination = "Europe"
    amount_spent = budget * 0.9
    type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {amount_spent:.2f}")
