def merge(a, b):
    return {**a, **b}


first_family = json.loads(input())
second_family = json.loads(input())

print(merge(first_family, second_family))
