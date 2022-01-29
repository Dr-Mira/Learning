import random

print('H A N G M A N')

options = ['python', 'java', 'kotlin', 'javascript']
selected_word = random.choice(options)

if str(input('Guess the word: ')) == selected_word:
    print('You survived!!')
else:
    print('You lost!')
