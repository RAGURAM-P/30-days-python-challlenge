import datetime
import time
alarm_time=input("Enter alarm time in HH:MM:SS format (24-hour): ")
print(f"alarm set for{alarm_time}")
while True:
    now=datetime.datetime.now().strftime("%H:%M:%S")
    if now==alarm_time:
        print("wake up its time!")
        break
    time.sleep(1)
