# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.


import math
hours = int(input())
minutes = int(input())
total = hours * 60 + minutes + 15
new_hours = total / 60
new_minutes = total % 60
new_hours = math.floor(new_hours)
if new_hours > 23:
    new_hours = 0
if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
    print(f"{new_hours}:{new_minutes}")
