city = input()
salles = float(input())
price = 0
if 0 <= salles <= 500 and city == "Sofia":
    price = 5
elif 0 <= salles <= 500 and city == "Varna":
    price = 4.5
elif 0 <= salles <= 500 and city == "Plovdiv":
    price = 5.5
if 500 < salles <= 1000 and city == "Sofia":
     price = 7
elif 500 < salles <= 1000 and city == "Varna":
     price = 7.5
elif 500 < salles <= 1000 and city == "Plovdiv":
     price = 8
if 1000 < salles <= 10000 and city == "Sofia":
    price = 8
elif 1000 < salles <= 10000 and city == "Varna":
    price = 10
elif 1000 < salles <= 10000 and city == "Plovdiv":
    price = 12
if salles > 10000 and city == "Sofia":
    price = 12
elif salles > 10000 and city == "Varna":
    price = 13
elif salles > 10000 and city == "Plovdiv":
    price = 14.5
if city == "Sofia" or city == "Plovdiv" or city == "Varna":
    if salles > 0:
       print(f"{salles * price / 100:.2f}")
    elif salles < 0:
        print("error")
else:
    print("error")