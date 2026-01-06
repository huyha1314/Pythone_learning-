import time
minute = 0
hour = 0


mytime = int(input("pls input your sleeping time in second"))
for x in range(mytime, 0, -1):
    second = x % 60
    total_minutes = x // 60
    hour = x // 3600
    minute = total_minutes - (hour * 60)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("WAKE UP!")
