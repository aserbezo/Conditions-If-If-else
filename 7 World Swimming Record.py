import math
record_in_sec = float(input())
distance_meter = float(input())
time_sec = float(input())
swim_distance = distance_meter * time_sec
resistance = distance_meter / 15
delay_time =math.floor(resistance) * 12.5
total_time = swim_distance + delay_time
if total_time >= record_in_sec:
    total_time -= record_in_sec
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")

elif total_time < record_in_sec:
    print(f" Yes, he succeeded! The new world record is {abs(total_time):.2f} seconds.")

