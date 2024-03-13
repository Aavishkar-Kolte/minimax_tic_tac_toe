class tic_tac_toe():
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_player = 'X'


    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()


    def check_winner(self):
        winners = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

        for i in winners:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] != ' ':
                return True

        return False


    def cat_scratch(self):
        return ' ' not in self.board


    def play(self):
        position = int(input(f"Player {self.current_player}'s turn, enter mark position: "))

        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid position")
            return False
        


