# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):
# Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
# Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
# Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
# Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и дължината на височината към нея.
# Резултатът да се закръгли до 3 цифри след десетичната точка.

figure = input()
if figure == "square":
    side = float(input())
    face = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    face = side_a * side_b
elif figure == "circle":
    from math import pi
    radius = float(input())
    diametur = radius + radius
    face = pi * radius * radius
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    face = (side_a * side_b) / 2
print(f"{face:.3f}")