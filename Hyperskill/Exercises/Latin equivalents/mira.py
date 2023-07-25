name = input()
original = ['é', 'ë', 'á', 'å', 'œ', 'æ']
new = ['e', 'e', 'a', 'a', 'oe', 'ae']


def normalize(a):
    for _ in a:
        i = 0
        for _ in original:
            new_name = a.replace(original[i], new[i])
            i += 1
    return new_name

print(normalize(name))