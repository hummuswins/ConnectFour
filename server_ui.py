# James Anh Minh Nguyen ID: 45298461    Kammy Deng ID: 72943066
#
# This module allows the player to connect to the server and
# play Connect Four against the Artificial Intelligence.

import connect_server
import c4_shared_function
import connectfour


def play_game(connection: connect_server.GameConnection, game_state: connectfour.GameState):
    '''
    Submitting the user moves into the game state. Get the response from the server. Interpret the
    server commands and print the board. Repeat the process until either the user or the server
    wins the game
    '''
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
    Asks for the user command. If user command is invalid, no changes will be done on the game state.
    If valid, sends the user command to the server, updates the game state, and prints out the
    updated game board. User will be promtp continuously until command is valid.
    '''

    user_command = input()
    while c4_shared_function.game_move(game_state, user_command) is None:
        user_command = input()

    connect_server.input_user_command(connection, user_command)
    game_state = c4_shared_function.game_move(game_state, user_command)
    
    print(c4_shared_function.board(game_state))

    return game_state


def start_game() -> connect_server.GameConnection:
    '''
    Starts the game by asking for a host and a port. The game will attempt to connect.
    If it fails to connect, the console will print why the server didn't connect,
    and prompt user to try again. If the username didn't work, the console will prompt
    the user to try using another username.
    '''
    while True:
        host = input('Please enter the IP Address or hostname you wish to connect to: ')
        port = input('Please specify which port you want to enter: ')
        try:
            # Connected is a boolean variable that is defined when a correct connection has been made.
            connected = False

            while connected is False:
                connection = connect_server.connect(host, int(port))
                username = input('Please input a username (no spaces or whitespace characters): ')
                connected = connect_server.start_connection(connection, username)

                # This line is for cases in which we can connect to a server, but not the connect four server.
                if connected is None:
                    print('Invalid Server Input, please try another host and port')
                    break

            if connected is True:
                break

        except Exception as Error:
            print(Error)
            continue

    print(
        'Welcome, ' + username + ' to AI Connect Four Game!\n'
        'In order to play the game, please type "DROP #" or '
        '"POP #" with # as the column that you want to drop or pop the piece!')
    return connection


def main():
    '''Run the server program'''
    connection = start_game()
    game_state = c4_shared_function.make_board()
    print(c4_shared_function.board(game_state))
    play_game(connection, game_state)


if __name__ == '__main__':
    main()
