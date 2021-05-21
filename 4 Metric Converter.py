# Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m.
# Използвайте съответствията от таблицата по-долу:
# входна единица	изходна единица
# 1 meter (m)	1000 millimeters (mm)
# 1 meter (m)	100 centimeters (cm)

first = float(input())
second = input()
third = input()

if second == "mm":
    second_mm = first
elif second == "cm":
    second_mm = first * 10
else:
    second_mm =first * 1000
if third == "mm":
   third_mm = second_mm
elif third == "cm":
    third_mm = second_mm / 10
else:
    third_mm = second_mm / 1000

print(f"{third_mm:.3f}")
