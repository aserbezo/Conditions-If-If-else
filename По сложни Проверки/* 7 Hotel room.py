month = input()
days = int(input())
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if days > -1 and days <= 7:
        apartment_n = apartment
        studio_n = studio
    elif days > 7 and days <= 14:
        studio_n = studio - (studio * 0.05)
        apartment_n = apartment
    elif days > 14:
        studio_n = studio - (studio * 0.3)
        apartment_n = apartment - (apartment * 0.1)
if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if days > -1 and days <= 14:
        studio_n = studio
        apartment_n = apartment
    elif days > 14:
        studio_n = studio - (studio * 0.2)
        apartment_n = apartment - (apartment * 0.1)
if month == "July" or month == "August":
    studio = 76
    apartment = 77
    if days > -1 and days <= 14:
        studio_n = studio
        apartment_n = apartment
    elif days > 14:
        studio_n = studio
        apartment_n = apartment - (apartment * 0.1)
print(f"Apartment: {apartment_n * days:.2f} lv.")
print(f"Studio: {studio_n * days :.2f} lv.")