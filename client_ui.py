# Playing with another player on own computer
import c4_shared_function
import connectfour
import sys

def play_game(game_state: connectfour.GameState):
    ''' Tells the user the correct input format for the game,
    and starts playing the game with the server. It will also let
    the user know who is the winner when the game is over.
    '''
    print('Welcome! In order to play the game, please type "DROP #" or "POP #" with # as the column that you want to drop or pop the piece!')
    print(c4_shared_function.board(game_state))
    
    while True:
        user_command = input()
        game_state = c4_shared_function.user_input(game_state, user_command)
        print(c4_shared_function.board(game_state))

        
        if connectfour.winner(game_state) == connectfour.RED:
            print('WINNER_RED')
            sys.exit()
        elif connectfour.winner(game_state) == connectfour.YELLOW:
            print('WINNER_YELLOW')
            sys.exit()


def main():
    ''' Calls the following functions if it starts in the main function
    '''
    game_state = c4_shared_function.make_board()
    play_game(game_state)

    
if __name__ == '__main__':
    main()
