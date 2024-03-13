from tic_tac_toe import *

if __name__ == "__main__":
    game_mode = input("Enter game mode (1 for Human vs Human, 2 for Human vs AI): ")

    if game_mode == "1":
        game = TicTacToeHumanVsHuman()
    elif game_mode == "2":
        game = TicTacToeHumanVsAI()
    else:
        print("Invalid game mode. Exiting...")
        exit()

    print("TIC TAC TOE\n")

    game.start()
