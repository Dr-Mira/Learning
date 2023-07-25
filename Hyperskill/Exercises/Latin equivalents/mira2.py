name = input()

dictionary = {1: ['é', 'e'],
              2: ['ë', 'e'],
              3: ['á', 'a'],
              4: ['å', 'a'],
              5: ['œ', 'oe'],
              6: ['æ', 'ae']}

def normalize(a):
    a = a.replace(dictionary[1][0], dictionary[1][1])
    a = a.replace(dictionary[2][0], dictionary[2][1])
    return a

print(normalize(name))