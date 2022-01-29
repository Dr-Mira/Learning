import random


def occurrences(a, b):                  # finds overlaping number of sequences of substring b in string
    i = start = 0                       # and returns dictionary with
    while True:
        start = a.find(b, start) + 1
        if start > 0:
            i += 1
        else:
            return i


def percentage(a, b, c):
    i, j = 0, 0
    k = len(a) - 3                      # lenght of test string short of 3, because we dont evaluate first three symbols
    for _ in range(k):                  # compares each symbol from 4th position onward
        if a[i + 3] == b[i + 3]:
            j = j + 1
        i += 1
    if c == 0:
        return j
    if c == 1:
        return k
    else:
        return round(100 * (j / k), 2)


def main():
    money = 1000
    data = ''
    result = {'000': [],
              '001': [],
              '010': [],
              '011': [],
              '100': [],
              '101': [],
              '110': [],
              '111': []}
    print('Please give AI some data to learn...')
    print(f'Current data length is {len(data)}, {100 - len(data)} symbols left')
    while len(data) < 100:
        print(f'Print a random string containing 0 or 1')
        x = input()
        data = data + x
        data = [x for x in data if x in '01']
        data = ''.join(data)
        print(f'Current data length is {len(data)}, {100 - len(data)} symbols left')

    print('Final data string:')
    print(data)
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print("""Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")

    while True:
        print('Print a random string containing 0 or 1')
        a = str(input())
        b = ''

        if a == 'enough':
            print('Game over!')
            exit()

        if not set(a) <= set('01'):     #checks if string is valid eg contains only '01' if invalid skip rest of code and iterate fresh
            continue

        for i in result:
            result_list = []
            for j in '01':
                result_list.append(occurrences(data, i + j))
            result[i] = result_list

        for _ in range(3):
            b = b + str(random.randint(0, 1))

        i = 0
        for _ in range(len(a) - 3):  # loop all triades starting from 4th position in test string
            x = result[a[i: i + 3]][0]  # number of '0' instances after selected triade
            y = result[a[i: i + 3]][1]  # number of '1' instances after selected triade

            if x == y:
                b = b + str(random.randint(0, 1))
            elif x > y:
                b = b + '0'
            elif x < y:
                b = b + '1'
            i += 1

        money = money - percentage(a, b, 0) + ((len(a) - 3) - percentage(a, b, 0))

        print('prediction:')
        print(f'{b}')
        print(f'Computer guessed right {percentage(a, b, 0)} out of {percentage(a, b, 1)} symbols ({percentage(a, b, 2)} %)')
        print(f'Your balance is now ${money}')


if __name__ == '__main__':
    main()

