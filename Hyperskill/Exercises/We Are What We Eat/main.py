result = 0
for x in meals:
    result = result + x.get('kcal')
print(result)
