# Python 3.7

import random

full_domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                   [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                   [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                   [3, 3], [3, 4], [3, 5], [3, 6],
                   [4, 4], [4, 5], [4, 6],
                   [5, 5], [5, 6],
                   [6, 6]]
random.shuffle(full_domino_set)


class DominoGame:

    def __init__(self):
        self.stock = full_domino_set[14:]           # pieces available in pool
        self.player = full_domino_set[0:7]          # pieces player have available at hand
        self.computer = full_domino_set[7:14]       # pieces computer have available at hand
        self.snake = []                             # list of pieces which are lying on the game table
        self.status = ''                            # who is supposed to make next move
        self.choice = 0                             # player choice of piece valid from -7 to 7 usually
        self.piece = []                             # selected piece from domino pool
        self.assign = ''                            # if piece will be assigned left or right of the snake
        self.rotate = False                         # if piece needed to be rotated before assignment
        self.move = False                           # if move is legal or not
        self.result = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}  # AI shit
        self.scored = {}

    def legal(self):    # checks if move is legal based on right or left move
        if self.assign == 'left':
            if self.snake[0][0] == self.piece[0] or self.snake[0][0] == self.piece[1]:
                self.move = True
            else:
                self.move = False
        elif self.assign == 'right':
            if self.snake[-1][-1] == self.piece[0] or self.snake[-1][-1] == self.piece[1]:
                self.move = True
            else:
                self.move = False
        if self.assign == 'new':
            self.move = True

    def the_ai(self):
        self.scored.clear()
        self.assign = 'right'
        for i in self.computer + self.snake:    # count occurrence of each number on the table + in computer hands
            for j in str(i):
                if j in self.result:
                    self.result[j] += 1
        for i in self.computer:    # gives score to each piece in computer hand
            for j in i:
                if str(i) in self.scored:
                    self.scored[str(i)] += self.result[str(j)]
                else:
                    self.scored[str(i)] = self.result[str(j)]

    def ai_choice(self):    # AI will choose integer same as player would
        x = max(self.scored, key=self.scored.get)    # selects piece with the highest ranking
        y = x.strip('][').split(', ')    # converts string to the list
        z = []
        for i in y:
            z.append(int(i))
        self.choice = self.computer.index(z) + 1    # number of computer selected piece and returns its number

    def rotation(self):    # decides whenever the piece have to be rotated, not rotated or if it can't be placed
        if self.assign == 'left':
            if self.snake[0][0] != self.piece[1]:
                self.piece = self.piece[::-1]
        if self.assign == 'right':
            if self.snake[-1][-1] != self.piece[0]:
                self.piece = self.piece[::-1]

    def put(self):    # decides whenever the user/pc wants to put piece left right or to take new piece
        if self.choice < 0:    # put left
            self.assign = 'left'
        elif self.choice > 0:    # put right
            self.assign = 'right'
        elif self.choice == 0:    # take piece from stock
            self.assign = 'new'

    def active_piece(self):    # selects which piece user/pc wants to add from their pool
        if self.status == 'player':
            self.piece = self.player[abs(self.choice) - 1]
        else:
            self.piece = self.computer[abs(self.choice - 1)]

    def starting_player(self):  # decides if computer or pc should start
        a = [x for x in self.player if x[0] == x[1]]
        b = [x for x in self.computer if x[0] == x[1]]
        c = a + [[0, 0]]    # artificial adding [0, 0] so even empty lists can be compared, I wanted to avoid extensive if
        d = b + [[0, 0]]
        if max(c) > max(d):
            self.player.remove(max(a))
            self.snake.append(max(a))
            self.status = 'computer'
        elif max(c) < max(d):
            self.computer.remove(max(b))
            self.snake.append(max(b))
            self.status = 'player'
        else:
            random.shuffle(full_domino_set)

    def display(self):    # display what player have at hand + how many pieces in stock are left
        print(70 * '=')
        print('Stock size:', len(self.stock))
        print('Computer pieces:', len(self.computer))
        x = ''
        for i in self.snake:
            x += str(i)
        if len(self.snake) > 6:
            print(f'{str(x)[0:18]}...{str(x)[-18:]}')
        else:
            print(str(x))
        print('Your pieces:')
        x = 1
        for i in self.player:
            print(f'{x}:{i}')
            x += 1
        print()

    def user_input(self):    # takes user input and validate if its valid
        if self.status == 'computer':
            print('Status: Computer is about to make a move. Press Enter to continue...')
            input()
            game.the_ai()
            while True:
                if self.scored == {}:
                    self.assign == 'new'
                    break
                game.ai_choice()
                game.put()
                game.active_piece()
                game.rotation()
                game.legal()
                if self.move:
                    break
                elif not self.move:
                    if self.rotate:
                        self.scored.pop(str(self.piece))
                    elif not self.rotate:
                        self.scored.pop(str(self.piece[::-1]))

        else:
            print("Status: It's your turn to make a move. Enter your command.")
            while True:
                try:
                    self.choice = int(input())
                    game.put()
                    game.active_piece()
                    game.rotation()
                    game.legal()
                    x = len(self.player)
                    if abs(self.choice) not in range(x + 1):
                        print('Invalid input. Please try again.')
                    elif self.move is False:
                        print('Illegal move. Please try again.')
                    else:
                        break
                except:
                    print('Invalid input. Please try again.')

    def action(self):    # perform the action of adding new piece to the growing snake
        if self.status == 'player':
            if self.assign == 'left':
                self.snake = [self.piece] + self.snake
                self.player.pop(abs(self.choice) - 1)
            elif self.assign == 'right':
                self.snake.append(self.piece)
                self.player.pop(abs(self.choice) - 1)
            elif self.assign == 'new':
                x = self.stock[0]
                self.player.append(x)
                self.stock.remove(x)
            self.status = 'computer'
        elif self.status == 'computer':
            if self.assign == 'left':
                self.snake = [self.piece] + self.snake
                self.computer.pop(abs(self.choice) - 1)
            elif self.assign == 'right':
                self.snake.append(self.piece)
                self.computer.pop(abs(self.choice) - 1)
            elif self.assign == 'new':
                x = self.stock[0]
                self.computer.append(x)
                self.stock.remove(x)
            self.status = 'player'

    def endgame(self):    # each turn checks if winning condition is met for either player
        if not self.computer:
            game.display()
            print('Status: The game is over. The computer won!')
            exit()
        elif not self.player:
            game.display()
            print('Status: The game is over. You won!')
            exit()
        elif len(self.stock) == 0:
            game.display()
            print('Draw')
            print()


if __name__ == '__main__':
    game = DominoGame()
    game.starting_player()
    while True:
        game.display()
        game.user_input()
        game.action()
        game.endgame()
