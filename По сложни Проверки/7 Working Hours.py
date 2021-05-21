time = int(input())
text = input()

if text == "Monday" or text == "Tuesday" or text == "Wednesday" or text == "Thursday" or text == "Friday" or text == "Saturday":
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")