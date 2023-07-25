x, y = int(input()), int(input())

if x == 1 or x == 8:
    if y == 1 or y == 8:
        result = 3
    else:
        result = 5
elif y == 1 or y == 8:
    if x == 1 or x == 8:
        result = 3
    else:
        result = 5
else:
    result = 8

print(result)
