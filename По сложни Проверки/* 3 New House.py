flowers = input()
numbers = int(input())
budget = float(input())
sum = 0
if flowers == "Roses":
    if numbers > 80:
        sum = (numbers * 5) *0.9
    else:
        sum = numbers * 5
if flowers == "Dahlias":
    if numbers > 90:
        sum = (numbers * 3.8) *0.85
    else:
        sum = numbers * 3.8
if flowers == "Tulips":
    if numbers > 80:
        sum = (numbers * 2.8)*0.85
    else:
        sum = numbers * 2.8
if flowers == "Narcissus":
    if numbers < 120:
        sum = numbers * 3 + (numbers * 3)*0.15
    else:
        sum = numbers * 3
if flowers == "Gladiolus":
    if numbers < 80:
        sum = numbers * 2.5 + (numbers * 2.5)*0.2
    else:
        sum = numbers * 2.5
if budget >= sum:
    print(f"Hey, you have a great garden with {numbers} {flowers} and {(budget - sum):.2f} leva left.")
elif budget < sum:
    print(f"Not enough money, you need {abs(budget - sum):.2f} leva more.")