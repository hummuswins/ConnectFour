# Play connect four against Artificial Intelligence

import connect_server
import c4_shared_function
import connectfour


def play_game(connection: connect_server.GameConnection, game_state: connectfour.GameState):
    while True:
        # This is printing out the user input and submitting the input to the server
        game_state = user_input(connection, game_state)

        # This is getting the response from the server and printing it out
        response = connect_server.read_server_input(connection)

        print(response[0])
        if response[0] == 'WINNER_RED':
            return
        elif response[0] == 'INVALID':
            continue
        else:
            game_state = c4_shared_function.game_move(game_state, response[0])
            if response[1] == 'WINNER_YELLOW':
                print(c4_shared_function.board(game_state))
                print(response[1])
                return

        print(c4_shared_function.board(game_state))


def user_input(connection: connect_server.GameConnection, game_state: connectfour.GameState) -> connectfour.GameState:
    '''
    Get user input. Make sure user input is valid. If valid, execute the user command into the server and
    return the current game state. If not valid, the user input another command.
    '''

    user_command = input()
    while c4_shared_function.game_move(game_state, user_command) is None:
        user_command = input()

    connect_server.input_user_command(connection, user_command)

    game_state = c4_shared_function.game_move(game_state, user_command)
    print(c4_shared_function.board(game_state))

    return game_state


def main():
    # Check if server will accepts username. If it doesn't, redo the loop and ask for another username
    while True:
        connection = connect_server.connect('woodhouse.ics.uci.edu', 4444)
        username = input('What is your username? ')
        if connect_server.start_game(connection, username):
            break
        print('Invalid Username (no spaces)')

    print(
        'Welcome, ' + username + ' to AI Connect Four Game!\n'
        'In order to play the game, please type "DROP #" or '
        '"POP #" with # as the column that you want to drop or pop the piece!')

    game_state = c4_shared_function.make_board()
    print(c4_shared_function.board(game_state))
    play_game(connection, game_state)


if __name__ == '__main__':
    main()
