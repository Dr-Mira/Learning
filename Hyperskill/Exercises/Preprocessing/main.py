x = str(input())
for i in ',.!?':
    x = x.replace(i, '')
print(x.lower())
