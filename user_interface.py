import connectfour
import collections
import sys


def make_board() -> connectfour.GameState:
    '''
    Initialize the game board into our global variable
    '''
    game_state = connectfour.new_game()
    return game_state


def board(game_state: connectfour.GameState) -> str:
    ''' Creates a new game board for the game in the beginning
    and keeps track of the status of the game board. 
    '''
    board = game_state.board
    string = ''
    for x in range(0, connectfour.BOARD_COLUMNS):
        string += str(x + 1) + ' '
    string += '\n'
    
    for x in range(0, connectfour.BOARD_ROWS):
        for y in range(0, connectfour.BOARD_COLUMNS):
            if board[y][x] == 0:
                string += '. '
            elif board[y][x] == 1:
                string += 'R '
            elif board[y][x] == 2:
                string += 'Y '
            else:
                print('invalid value')
                break
                
        string += '\n'
    
    return string


def user_input(game_state: connectfour.GameState, user_command: str) -> connectfour.GameState:
    ''' Identifying whether the user wants to drop or pop its piece
    in its his/her desired column. Returning Invaid Move Commands if
    the column number entered is out of range.
    '''

    try:
        if user_command[0:4] == 'DROP':
            column = int(user_command[5]) - 1
            game_state = connectfour.drop(game_state, column)
            
        elif user_command[0:4] == 'POP ':
            column = int(user_command[4])
            game_state = connectfour.pop(game_state, column)
            
        else:
            print('Error, Invalid Commands')
    
    except connectfour.InvalidMoveError:
        print('Invalid Move Error')
        
    except IndexError:
        print('Index Error')
        
    finally:
        return game_state
        


def play_game(game_state: connectfour.GameState):
    ''' Tells the user the correct input format for the game,
    and starts playing the game with the server. It will also let
    the user know who is the winner when the game is over.
    '''
    print('Welcome! In order to play the game, please type "DROP #" or "POP #" with # as the column that you want to drop or pop the piece!')
    print(board(game_state))
    
    while True:
        user_command = input()
        game_state = user_input(game_state, user_command)
        print(board(game_state))

        if connectfour.winner(game_state) == connectfour.RED:
            print('WINNER_RED')
            sys.exit()
        elif connectfour.winner(game_state) == connectfour.YELLOW:
            print('WINNER_YELLOW')
            sys.exit()


def main():
    ''' Calls the following functions if it starts in the main function
    '''
    game_state = make_board()
    play_game(game_state)

    
if __name__ == '__main__':
    main()
    
