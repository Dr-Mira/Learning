def first_factorial(num):
    if num == 1:
        return num
    return num * first_factorial(num - 1)


x = int(input())
print(first_factorial(x))
