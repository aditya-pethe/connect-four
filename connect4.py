# cli connect four game as a standalone project

class connect4:

    def __init__(self):
        
        self.size = 7
        self.state = "undecided"
        self.board = [[" " for i in range(self.size)] for i in range(self.size)]
        self.turn = "Player 1 [X]"
        self.piece = "X"
        self.visited = set()

        pass

    def switch_turn(self):

        if self.turn == "Player 1 [X]":
            self.turn = "Player 2 [O]"
            self.piece = "O"
        else:
            self.turn = "Player 1 [X]"
            self.piece = "X"

    def print_board(self):

        print(f"It's {self.turn}'s turn! \n")
        print([f"{i}" for i in range(self.size)])
        print('\n')
        for row in self.board:
            print(row)
        print('\n')

        

    def place(self, column) -> None:

        place_row = -1

        for row in range(self.size):

            if self.board[row][column] == ' ':
                place_row = row
            else:
                place_row = row - 1
                break
        
        if place_row == -1:
            print("\nThis column is full - you can't place a piece here\n")
        else:
            self.board[place_row][column] = self.piece
            self.visited.add((place_row, column))
        

    def find_longest_streak(self, i, j, increment):

        right_i, right_j = increment
        left_i = -1 * right_i
        left_j = -1 * right_j

        left_streak = 0
        right_streak = 0

        current_piece = self.board[i][j]

        row,col = i,j

        while self.is_valid_index(row,col) and self.board[row][col] == current_piece:

            row += right_i
            col += right_j
            right_streak += 1

        while self.is_valid_index(row,col) and self.board[row][col] == current_piece:

            row += left_i
            col += left_j
            left_streak += 1

        return left_streak + right_streak
    

    def check_if_win(self):

        for i,j in self.visited:

            current_piece = self.board[i][j]
            longest = 1

            for increment in [
                (1,0), # up-down
                (0,1), # left-right
                (1,1), # diag like \
                (1,-1) # diag like /
            ]:

                streak = self.find_longest_streak(i,j,increment)

                if streak == 4:
                    self.game_over()
                    return True

    def is_valid_index(self,i,j):

        if i >= 0 and i < self.size:
            if j >= 0 and j < self.size:
                return True
            else:
                return False

    def game_over(self):
        self.state = "finished"
        print(f"GAME OVER! {self.turn} WINS!")

    def get_game_state(self):
        return self.state

    def reset_game(self):
        
        self.size = 7
        self.state = "undecided"
        self.board = [[" " for i in range(self.size)] for i in range(self.size)]
        self.turn = "Player 1 [X]"
        self.piece = "X"
        self.visited = set()










