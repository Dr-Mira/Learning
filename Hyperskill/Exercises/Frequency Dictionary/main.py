import time
start_time = time.time()
x = ('a aa abC aa ac abc bcd a'*10000).lower().split()


for i in set(x):
    print(i, x.count(i))
