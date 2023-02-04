hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = dura + mins + (hour * 60)

end_mins = total_mins % 60

end_hour = (total_mins // 60) % 24

print(end_hour, ":", end_mins)
