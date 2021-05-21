days = int(input()) - 1
type_room = input()
evaluation = input()
room_one_person = 18
apartment = 25.00
president_apartment = 35
if days < 10 and type_room == "apartment":
    price = days * apartment
    discount = price - (price * 0.3)
elif days < 10 and type_room == "president apartment":
    price = days * president_apartment
    discount = price - (price * 0.1)
elif 10 <= days <= 15 and type_room =="apartment":
    price = days * apartment
    discount = price - (price * 0.35)
elif 10 <= days <= 15 and type_room == "president apartment":
    price = days * president_apartment
    discount = price - (price * 0.15)
elif days > 15 and type_room == "apartment":
     price = days * apartment
     discount = price - (price * 0.50)
elif days > 15 and type_room == "president apartment":
     price = days * president_apartment
     discount = price - (price * 0.20)
else:
    type_room == "room for one person"
    price = days * room_one_person
    discount = price
if evaluation == "positive":
    final = discount + (discount * 0.25)
    print(f"{final:.2f}")
elif evaluation == "negative":
    final = discount - (discount * 0.1)
    print(f"{final:.2f}")





