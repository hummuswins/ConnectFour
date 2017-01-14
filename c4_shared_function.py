# James Anh Minh Nguyen ID: 45298461    Kammy Deng ID: 72943066
#
# This module consists of shared functions in the ConnectFour Game
# This includes functions that creates a standard game board and
# interprets the player's move. 


import connectfour


def make_board() -> connectfour.GameState:
    '''
    Creates a new game state for a new game.
    '''
    game_state = connectfour.new_game()
    return game_state


def board(game_state: connectfour.GameState) -> str:
    '''Goes into the GameState namedtuple to fill in the space with R
    for RED player's move and Y for YELLOW player's move. Returns a presentable
    game board.
    '''
    board = game_state.board
    string = ''
    for number in range(0, connectfour.BOARD_COLUMNS):
        string += str(number + 1) + ' '
    string += '\n'
    
    for row in range(0, connectfour.BOARD_ROWS):
        for column in range(0, connectfour.BOARD_COLUMNS):
            if board[column][row] == 0:
                string += '. '
            elif board[column][row] == 1:
                string += 'R '
            elif board[column][row] == 2:
                string += 'Y '
            else:
                print('Invalid Value')
                break
                
        string += '\n'
    
    return string


def game_move(game_state: connectfour.GameState, user_command: str) -> connectfour.GameState:
    ''' Identify the player's move. Whether he wants to drop or pop his piece and
    in which column. Prints out different types of error messages when the input is invalid
    Promtps the player to input again. Stores the moves in the GameState namedtuple. 
    '''

    try:
        if int(user_command[5:]) <= int(7):
            if user_command[0:4] == 'DROP':
                    column = int(user_command[5]) - 1
                    game_state = connectfour.drop(game_state, column)
                
            elif user_command[0:3] == 'POP':
                    column = int(user_command[4]) - 1
                    game_state = connectfour.pop(game_state, column)

        else:
            print('Error. Please choose a number between 1 and 7')
            return 
        return game_state

    except connectfour.InvalidMoveError:
        print("Invalid Move")
        return

    except IndexError:
        print('DROP or POP must be followed by a space and a number')
        return

    except ValueError:
        print('Not a valid command. Please choose a number between 1 and 7\n'
              'and put the number in the following format "DROP #" or "POP #".')
        return

    except TypeError:
        return

