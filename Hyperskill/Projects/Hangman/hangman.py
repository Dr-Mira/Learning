import random


def game():
    options = ['python', 'java', 'kotlin', 'javascript']
    letters = ("abcdefghijklmnopqrstuvwxyz")
    list_of_guesses = []
    word = random.choice(options)
    print()
    print(len(word) * "-")
    lives_left = 8

    while lives_left > 0:
        guess = input("Input a letter: ")
        result = []
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in letters and len(guess) == 1:
            print("Please enter a lowercase English letter")
        elif guess not in word and guess not in list_of_guesses:
            print("That letter doesn't appear in the word")
            lives_left -= 1
        elif guess in list_of_guesses:
            print("You've already guessed this letter")
        list_of_guesses.append(guess)
        for i in word:
            if i in list_of_guesses:
                result.append(i)
            else:
                result.append("-")
        x = "".join(result)
        if lives_left == 0:
            print("You lost!\n")
            main()
        if x == word:
            print("You guessed the word!")
            print("You survived!\n")
            main()
        print()
        print(x)


def main():
    print('H A N G M A N')
    while True:
        a = str(input('Type "play" to play the game, "exit" to quit: '))
        if a == "play":
            game()
        elif a == "exit":
            exit()


if __name__ == "__main__":
    main()
