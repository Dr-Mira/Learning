a, b, operator = float(input()), float(input()), input()

if b == 0 and operator in ["/", "mod", "div"]:
    print("Division by 0!")
elif operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "/":
    print(a / b)
elif operator == "*":
    print(a * b)
elif operator == "mod":
    print(a % b)
elif operator == "pow":
    print(a ** b)
elif operator == "div":
    print(a // b)
