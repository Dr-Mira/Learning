d = 1000
v1 = 1


def average_speed(v1, ratio):
    v2 = v1 * ratio
    t1 = d / v1
    t2 = d / v2
    v_average = (2 * d) / (t1 + t2)
    return v_average


for i in range(1, 1000):
    print(f'ratio v1:v2, 1:{i}, average speed: {round(average_speed(v1, i), 6)}')
