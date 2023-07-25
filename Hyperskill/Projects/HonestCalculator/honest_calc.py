msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


operation = {"+": (lambda x, y: x + y),
             "-": (lambda x, y: x - y),
             "*": (lambda x, y: x * y),
             "/": (lambda x, y: x / y)}


def is_operator(a):
    return a in '+-*/'


def is_valid(a):           # returns True if int, float or M, False for everything else
    a = str(a)
    a = a.replace('.', '')
    b = a.isnumeric()
    if a == 'M' or b:
        return True
    else:
        return False


def is_one_digit(a):
    if abs(a) in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
        return True
    else:
        return False


class Calculator:
    def __init__(self):
        self.x = 0
        self.oper = ''
        self.y = 0
        self.result = 0
        self.memory = 0
        self.restart = False

    def input_to_float(self):
        self.x = float(self.x)
        self.y = float(self.y)

    def input_handler(self):
        while True:
            print(msg_0)
            self.x, self.oper, self.y = str(input()).split(' ')
            if self.x == 'M':
                self.x = self.memory
            if self.y == 'M':
                self.y = self.memory
            if not is_valid(self.x) or not is_valid(self.y):
                print(msg_1)
            elif not is_operator(self.oper):
                print(msg_2)
            else:
                break

    def calculation(self):
        self.restart = False
        if self.oper == '/' and self.y == 0:
            print(msg_3)
            self.restart = True
        else:
            self.result = operation[self.oper](float(self.x), float(self.y))

    def memory_handler(self):           # piece of art
        while True:
            print(msg_4)
            a = str(input())
            if a == 'y':
                if is_one_digit(self.result):
                    print(msg_10)
                    if input() == 'y':
                        print(msg_11)
                        if input() == 'y':
                            print(msg_12)
                            if input() == 'y':
                                self.memory = str(self.result)
                                return
                            else:
                                return
                        else:
                            return
                    else:
                        return
                else:
                    self.memory = str(self.result)
                    return
            elif a == 'n':
                return

    def next_round(self):
        while True:
            print(msg_5)
            a = str(input())
            if a == 'y':
                self.restart = True
                return
            elif a == 'n':
                exit()

    def check(self):
        msg = ''
        if is_one_digit(float(self.x)) and is_one_digit(float(self.y)):
            msg = msg + msg_6
        if float(self.x) == 1.0 or float(self.y) == 1.0:
            msg = msg + msg_7
        if (float(self.x) == 0.0 or float(self.y) == 0.0) and (self.oper == '*' or self.oper == '+' or self.oper == '-'):
            msg = msg + msg_8
        if msg != '':
            msg = msg_9 + msg
            print(msg)


if __name__ == '__main__':
    calc = Calculator()
    while True:
        calc.input_handler()
        calc.check()
        calc.calculation()
        if calc.restart is True:
            continue
        print(calc.result)
        calc.memory_handler()
        calc.next_round()
        if calc.restart is True:
            continue
