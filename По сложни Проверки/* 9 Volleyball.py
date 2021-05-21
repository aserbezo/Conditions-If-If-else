year =input()
p = int(input())
h = int(input())
import math
week = 48 - h
saturday_games = week * 3 / 4
week_home = h
holiday = p * 2 / 3
games = saturday_games + holiday + week_home
if year == "leap":
    extra = games + (games * 0.15)
elif year == "normal":
    extra = games
print(math.floor(extra))


