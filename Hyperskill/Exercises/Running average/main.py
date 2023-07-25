x = [int(i) for i in input()]
result = []

for i, j in enumerate(x):
    if i > 0:
        result.append((j + x[i-1])/2)

print(result)
