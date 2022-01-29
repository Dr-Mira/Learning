class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def buy_coffee(self, water, milk, beans, cups, money):
        a = self.water > water
        b = self.milk > milk
        c = self.beans > beans
        d = self.cups > cups

        if a and b and c and d:
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= cups
            self.money += money
            print('I have enough resources, making you a coffee!')
        else:
            print(f'Sorry, not enough resources!')

    def display(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


machine = CoffeeMachine()


def main():
    print('Write action (buy, fill, take, remaining, exit):')
    x = str(input())
    if x == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        x = str(input())
        if x == 'back':
            main()
        else:
            if x == '1':
                machine.buy_coffee(250, 0, 16, 1, 4)
            elif x == '2':
                machine.buy_coffee(350, 75, 20, 1, 7)
            elif x == '3':
                machine.buy_coffee(200, 100, 12, 1, 6)

    elif x == 'fill':
        print('Write how many ml of water you want to add:')
        water = int(input())
        print('Write how many ml of milk you want to add:')
        milk = int(input())
        print('Write how many grams of coffee beans you want to add:')
        beans = int(input())
        print('Write how many disposable coffee cups you want to add:')
        cups = int(input())
        machine.fill(water, milk, beans, cups)
    elif x == 'take':
        machine.take()
    elif x == 'remaining':
        machine.display()
    elif x == 'exit':
        exit()


if __name__ == '__main__':
    while True:
        main()
