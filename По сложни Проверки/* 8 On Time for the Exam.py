hour_exam = int(input())
min_exam = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_time = hour_exam * 60 + min_exam
arrive_time = arrive_hour * 60 + arrive_min

if arrive_time > exam_time:
    print("Late")
elif exam_time - arrive_time <= 30:
    print("On time")
else:
    print("Early")

final = abs(exam_time - arrive_time)
if exam_time - arrive_time > 0:
    if final < 60:
        print(f"{final} minutes before the start")
    else:
        print(f"{final // 60}:{final % 60:02d} hours before the start")
elif arrive_time - exam_time > 0:
    if final < 60:
        print(f"{final} minutes after the start")
    else:
        print(f"{final // 60}:{final % 60:02d} hours after the start")