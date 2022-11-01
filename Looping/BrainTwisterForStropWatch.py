'''
Designing a stop watch using looping construct
'''

import time
time_in_mins = int(input("Enter minutes: "))
time_in_secs = int(input("Enter seconds: "))

for each_sec in range (1, (time_in_mins * 60) + 1):
    time.sleep(1)
    if each_sec < 60:
        print(f"{each_sec} seconds")
    else:
        min = each_sec // 60
        sec = each_sec % 60
        print(f"{min} minutes {sec} seconds")
else:
    for remaining_sec in range(1, time_in_secs + 1):
        time.sleep(1)
        print(f"{time_in_mins} minutes {remaining_sec} seconds")




