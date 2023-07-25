x = int(input())

if x < 1:
    print('no army')
elif 1 <= x <= 9:
    print('few')
elif 10 <= x <= 49:
    print('pack')
elif 50 <= x <= 499:
    print('horde')
elif 500 <= x <= 999:
    print('swarm')
elif x >= 1000:
    print('legion')
