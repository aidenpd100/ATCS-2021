import random


class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append(['-', '-', '-'])

    def print_instructions(self):
        print('Welcome to TicTacToe!\nPlayer 1 is X and Player 2 is 0\nTake turns placing your pieces '
              '- the first to 3 in a row wins!')
        self.depth = int(input('AI Depth: '))

    def print_board(self):
        print('   0  1  2')
        for i in range(3):
            print(str(i) + '  ' + self.board[i][0] + '  ' + self.board[i][1] + '  ' + self.board[i][2])
        print()

    def is_valid_move(self, row, col):
        if (0 <= row <= 2) and (0 <= col <= 2) and (self.board[row][col] == '-'):
            return True
        return False

    def place_player(self, player, row, col):
        self.board[row][col] = player

    def take_manual_turn(self, player):
        row = int(input('Enter a row: '))
        col = int(input('Enter a column: '))

        while not self.is_valid_move(row, col):
            print('Please enter a valid move.')
            row = int(input('Enter a row: '))
            col = int(input('Enter a column: '))

        self.place_player(player, row, col)
        self.print_board()

    def minimax(self, player, depth):
        # base case
        if self.check_win('O'):
            return (10, None, None)
        elif self.check_win('X'):
            return (-10, None, None)
        elif self.check_tie():
            return (0, None, None)
        elif depth == 0:
            return (0, None, None)

        # recursive case
        opt_row = -1
        opt_col = -1
        if player == 'O':
            best = -100
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player('O', row, col)
                        score = self.minimax('X', depth-1)[0]
                        if score > best:
                            best = score
                            opt_row = row
                            opt_col = col
                        self.place_player('-', row, col)
            return (best, opt_row, opt_col)

        elif player == 'X':
            worst = 100
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == '-':
                        self.place_player('X', row, col)
                        score = self.minimax('O', depth-1)[0]
                        if score < worst:
                            worst = score
                            opt_row = row
                            opt_col = col
                        self.place_player('-', row, col)
            return (worst, opt_row, opt_col)

    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player, self.depth)
        print(score, row, col)
        self.place_player('O', row, col)
        self.print_board()

    def take_random_turn(self, player):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        while not self.is_valid_move(row, col):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        self.place_player(player, row, col)
        self.print_board()

    def take_turn(self, player):
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn(player)
        elif player == 'O':
            self.take_minimax_turn(player)

    def check_col_win(self, player):
        for col in range(3):
            if (self.board[0][col] == player) and (self.board[1][col] == player) and (self.board[2][col] == player):
                return True
        return False

    def check_row_win(self, player):
        for row in self.board:
            if (row[0] == player) and (row[1] == player) and (row[2] == player):
                return True
        return False

    def check_diag_win(self, player):
        if (self.board[0][0] == player) and (self.board[1][1] == player) and (self.board[2][2] == player) or (self.board[2][0] == player) and (self.board[1][1] == player) and (self.board[0][2] == player):
            return True
        return False

    def check_win(self, player):
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for col in row:
                if col == '-':
                    return False
        return True

    def play_game(self):
        game_over = False
        self.print_instructions()
        self.print_board()
        while not game_over:
            self.take_turn('X')
            if self.check_win('X'):
                game_over = True
                print('X WINS!')
            elif self.check_tie():
                game_over = True
                print('TIE!')

            if not game_over:
                self.take_turn('O')
            if self.check_win('O'):
                game_over = True
                print('O WINS!')