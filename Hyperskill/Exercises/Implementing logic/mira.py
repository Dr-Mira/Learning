def my_func():
    try:
        1 / 0
    except:
        1 / 0
    finally:
        return "It's OK."


print(my_func())