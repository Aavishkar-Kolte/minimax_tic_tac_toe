from tic_tac_toe import tic_tac_toe

if __name__ == "__main__":

    
    game = tic_tac_toe()
    print("TIC TAC TOE\n")

    while True:
        game.print_board()
    
        flag = game.play()

        if game.check_winner():
            game.print_board()
            print(f"Player {game.current_player} wins!")
            break
        elif game.cat_scratch():
            game.print_board()
            print("TIE")
            break

        if flag:
            if game.current_player == 'X':
                game.current_player ='O'
            else:
                game.current_player ='X'


        
