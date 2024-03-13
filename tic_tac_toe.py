class Player:
    def __init__(self, name):
        self.name = name
        self.mark = ""


class TicTacToeHumanVsHuman:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.player1 = Player(input("Enter player 1 name: "))
        self.player2 = Player(input("Enter player 2 name: "))
        self.player1.mark = "X"
        self.player2.mark = "O"
        self.current_player = self.player1

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        print()

    def check_winner(self, player):
        winners = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for i in winners:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] == player.mark:
                return True

        return False

    def cat_scratch(self):
        return " " not in self.board

    def play(self):
        position = int(
            input(f"Player {self.current_player.name}'s turn, enter mark position: ")
        )

        if self.board[position] == " ":
            if self.current_player == self.player1:
                self.board[position] = self.player1.mark
            else:
                self.board[position] = self.player2.mark
            return True
        else:
            print("Invalid position")
            return False

    def start(self):
        while True:
            self.print_board()

            valid_move = self.play()

            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player.name} wins!")
                break
            elif self.cat_scratch():
                self.print_board()
                print("TIE")
                break

            if valid_move:
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1


class TicTacToeHumanVsAI:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.human = Player(input("Enter player name: "))
        self.ai = Player("AI")
        self.human.mark = "X"
        self.ai.mark = "O"
        self.current_player = self.human
        self.empties = []

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        print()

    def check_winner(self, player):
        winners = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for i in winners:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] == player.mark:
                return True

        return False

    def find_empties(self):
        self.empties = [i for i in range(9) if self.board[i] == " "]

    def cat_scratch(self):
        return " " not in self.board

    def play(self):
        if self.current_player == self.human:
            position = int(
                input(
                    f"Player {self.current_player.name}'s turn, enter mark position: "
                )
            )
        else:
            print("AI's turn")
            position = self.minimax(self.ai)[1]

        if self.board[position] == " ":
            self.board[position] = self.current_player.mark
            return True
        else:
            print("Invalid position")
            return False

    def minimax(self, player):
        if self.check_winner(self.human):
            return -1, None
        elif self.check_winner(self.ai):
            return 1, None
        elif self.cat_scratch():
            return 0, None

        self.find_empties()

        if player == self.ai:
            best_score = -10000
            best_position = None
            for i in self.empties:
                self.board[i] = player.mark
                score, _ = self.minimax(self.human)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_position = i
            return best_score, best_position
        else:
            best_score = 10000
            best_position = None
            for i in self.empties:
                self.board[i] = player.mark
                score, _ = self.minimax(self.ai)
                self.board[i] = " "
                if score < best_score:
                    best_score = score
                    best_position = i
            return best_score, best_position

    def start(self):

        while True:
            self.print_board()

            valid_move = self.play()

            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player.name} wins!")
                break
            elif self.cat_scratch():
                self.print_board()
                print("TIE")
                break

            if valid_move:
                if self.current_player == self.human:
                    self.current_player = self.ai
                else:
                    self.current_player = self.human
