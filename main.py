from .demon import Demon
from .soldier import Soldier

class Game:
    def __init__(self):
        self.board = [[None for _ in range(10)] for _ in range(10)]

    def make_board(self, s):
        for j in range(len(s)):
            col = j % 10
            row = j // 10
            c = s[j]
            if c == 'S':
                self.board[row][col] = Soldier(row, col)
            elif c == '*':
                self.board[row][col] = Demon(row, col)

    def play_turn(self, current_turn):
        self.move_demons(current_turn)
        self.move_soldiers(current_turn)
        self.starve_demons()
        self.multiply_soldiers()
        self.multiply_demons()

    def move_demons(self, current_turn):
        for c in range(10):
            for r in range(10):
                if isinstance(self.board[r][c], Demon):
                    self.board[r][c].move(self.board, current_turn)

    def move_soldiers(self, current_turn):
        for c in range(10):
            for r in range(10):
                if isinstance(self.board[r][c], Soldier):
                    self.board[r][c].move(self.board, current_turn)

    def starve_demons(self):
        for c in range(10):
            for r in range(10):
                if isinstance(self.board[r][c], Demon):
                    self.board[r][c].starve(self.board)

    def multiply_soldiers(self):
        for c in range(10):
            for r in range(10):
                if isinstance(self.board[r][c], Soldier):
                    self.board[r][c].mult(self.board)

    def multiply_demons(self):
        for c in range(10):
            for r in range(10):
                if isinstance(self.board[r][c], Demon):
                    self.board[r][c].mult(self.board)

    def demons_win(self):
        return not any(isinstance(self.board[r][c], Soldier) for c in range(10) for r in range(10))

    def soldiers_win(self):
        return not any(isinstance(self.board[r][c], Demon) for c in range(10) for r in range(10))

    def play_game(self, random_string):
        self.make_board(random_string)
        current_turn = 1

        while not self.demons_win() and not self.soldiers_win() and current_turn < 20000:
            self.play_turn(current_turn)
            current_turn += 1

        return current_turn

def interstice(random_string):
    if len(random_string) != 100 or not all(c in "x*S" for c in random_string):
        raise ValueError("Input must be a 100-character string containing only 'x', '*', or 'S'.")

    game = Game()
    return game.play_game(random_string)
