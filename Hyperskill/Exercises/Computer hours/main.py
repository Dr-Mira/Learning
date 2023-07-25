# Make sure your output matches the assignment *exactly*
def computer_time(x):
    if x < 2:
        return "That seems reasonable"
    elif 2 <= x < 4:
        return "Do you have time for anything else?"
    else:
        return "Don't forget to take breaks!"


y = float(input())
print(computer_time(y))
