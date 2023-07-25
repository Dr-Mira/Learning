name = input()
dictionary = {1: ['é', 'e'],
              2: ['ë', 'e'],
              3: ['á', 'a'],
              4: ['å', 'a'],
              5: ['œ', 'oe'],
              6: ['æ', 'ae']}


def normalize(a):
    for i in dictionary:
        a = a.replace(dictionary[i][0], dictionary[i][1])
    return a
