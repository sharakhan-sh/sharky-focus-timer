import time
print(" Sharky says: small progress is still progress.")
work_hours = int(input(" Enter work hours (type 0 if you only want minutes): "))
work_minutes = int(input("Enter work minutes: "))
break_hours = int(input(" Enter break hours (type 0 if you only want minutes): "))
break_minutes = int(input(" Enter break minutes: "))

work_time = (work_hours * 3600) + (work_minutes * 60)
break_time = (break_hours * 3600) + (break_minutes * 60)

print("\n Work time!")
for i in range(work_time,0,-1):
       hours = i // 3600
       minutes = (i % 3600) // 60
       seconds = i % 60
       print(f"\r {hours:02}:{minutes:02}:{seconds:02}", end="")
       time.sleep(1)

print("\nBreak time!")
for i in range(break_time,0,-1):
          hours=i//3600
          minutes = (i % 3600) // 60
          seconds = i % 60
          print(f"\r {hours:02}:{minutes:02}:{seconds:02}", end="")
          time.sleep(1)

print("\n Sharky is proud of you.")
