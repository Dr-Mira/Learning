import random


def main():

    friends = []
    output = {}
    lucky_one = None

    class Bill:
        def __init__(self, name, value):
            self.name = name
            self.value = round(value, 2)
            if self.name == lucky_one:
                self.value = 0

        def create_dict(self):
            output[self.name] = self.value

    print('Enter the number of friends joining (including you):')
    number_of_people = int(input())

    if number_of_people < 1:
        print('No one is joining for the party')
        exit()

    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(number_of_people):
        friends.append(str(input()))

    print('Enter the total bill value:')
    total_bill_value = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/no:')
    choice = str(input())
    
    if choice == 'Yes':
        lucky_one = random.choice(friends)
        print(f'{lucky_one} is the lucky one!')
        number_of_people -= 1

    elif choice == 'No':
        print('No one is going to be lucky')
        
    for i in range(len(friends)):
        friends[i] = Bill(friends[i], total_bill_value / number_of_people)
        friends[i].create_dict()
            
    print(output)
        

if __name__ == '__main__':
    main()
