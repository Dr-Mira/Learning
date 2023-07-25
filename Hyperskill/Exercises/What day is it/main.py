list_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

offset = int(input())

if offset in range(-10, 14) or offset == 0:
    print(list_days[1])
elif offset < -10:
    print(list_days[0])
else:
    print(list_days[2])
