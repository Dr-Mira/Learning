import requests

cache = dict()
cache['eur'] = requests.get(f'http://www.floatrates.com/daily/eur.json').json()
cache['usd'] = requests.get(f'http://www.floatrates.com/daily/usd.json').json()

source_currency = input().lower()

if source_currency == 'EUR':
    r = cache['eur']
elif source_currency == 'USD':
    r = cache['usd']
else:
    r = requests.get(f'http://www.floatrates.com/daily/{source_currency}.json').json()
while True:
    target_currency = input().lower()
    if target_currency == '':
        exit()

    money_to_change = int(input())
    print('Checking the cache...')
    if target_currency in list(cache.keys()):
        print('Oh! It is in the cache!!')
        result = cache[source_currency.lower()][target_currency.lower()]['rate'] * money_to_change
        print(f'You received {round(result, 2)} {target_currency.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        result = r[target_currency]['rate'] * money_to_change
        print(f'You received {round(result, 2)} {target_currency.upper()}.')
        cache[target_currency] = r[target_currency]

