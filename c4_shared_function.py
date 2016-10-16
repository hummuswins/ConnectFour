import connectfour


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


def game_move(game_state: connectfour.GameState, user_command: str) -> connectfour.GameState:
    ''' Identifying whether the user wants to drop or pop its piece
    in its his/her desired column. Returning InvaLid Move Commands if
    the column number entered is out of range.
    '''

    try:
        if user_command[0:4] == 'DROP':
            column = int(user_command[5]) - 1
            game_state = connectfour.drop(game_state, column)
            
        elif user_command[0:4] == 'POP ':
            column = int(user_command[4]) - 1
            game_state = connectfour.pop(game_state, column)

        else:
            print('ERROR')
            return

        return game_state

    except connectfour.InvalidMoveError:
        print("INVALID_MOVE_ERROR")
        return

    except (IndexError, ValueError) as e:
        print(e)
        return


