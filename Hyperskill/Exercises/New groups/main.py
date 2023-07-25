n_groups = int(input())
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
kids = []
dict_classes = {'1A': None, '1B': None, '1C': None,
                '2A': None, '2B': None, '2C': None,
                '3A': None, '3B': None, '3C': None}

for i in range(n_groups):
    kids.append(int(input()))
    dict_classes[groups[i]] = kids[i]

print(dict_classes)
