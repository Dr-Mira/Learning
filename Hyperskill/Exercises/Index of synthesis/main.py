language_list = ["Analytic", "Synthetic", "Polysynthetic"]

x = float(input())

if x < 2:
    print(language_list[0])
elif 2 <= x <= 3:
    print(language_list[1])
elif x > 3:
    print(language_list[2])
