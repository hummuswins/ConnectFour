# This is the module that will connect with server

from collections import namedtuple
import socket

GameConnection = namedtuple(
    'GameConnection',
    ['socket', 'input', 'output'])


def connect(host: str, port: int) -> GameConnection:
    ''' Connects to the identified host and port, writes
    the user input into a readable message for the server,
    reads from the server's output, and return the socket,
    input, output as a namedtuple
    '''
    game_socket = socket.socket()
    game_socket.connect((host, port))

    game_input = game_socket.makefile('r')
    game_output = game_socket.makefile('w')

    return GameConnection(game_socket, game_input, game_output)


def start_game(connection: GameConnection, username: str) -> bool:
    '''Starts the game with a given username. If the game
    successfully started returns TRUE. If not, it closes the game
    '''
    command = 'I32CFSP_HELLO ' + username
    _write_line(connection, command)
    first_response = _read_line(connection)

    if first_response == 'WELCOME ' + username:
        _write_line(connection, 'AI_GAME')
        second_response = _read_line(connection)

        if second_response == 'READY':
            return True

    elif first_response == 'ERROR':
        return False

    close(connection)


def input_user_command(connection: GameConnection, user_command: str) -> None:
    '''

    '''
    _write_line(connection, user_command)


def read_server_input(connection: GameConnection) -> str:
    first_response = _read_line(connection)

    if first_response == 'OKAY':
        second_response = _read_line(connection)
        third_response = _read_line(connection)
        if third_response == 'READY':
            return second_response
        else:
            close(connection)
            return

    elif first_response == 'WINNER_RED' or 'WINNER_YELLOW':
        return first_response

    elif first_response == 'INVALID' or 'ERROR':
        second_response = _read_line(connection)
        if second_response == 'READY':
            return first_response
        else:
            close(connection)
            return


def close(connection: GameConnection) -> None:
    ''' It closes all the connection with the server
    '''
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def _write_line(connection: GameConnection, command: str) -> None:
    '''From the identified connection, it transforms user input/ statement
    into readable message for the server
    '''
    connection.output.write(command + '\r\n')
    connection.output.flush()


def _read_line(connection: GameConnection) -> str:
    '''From the identified connection, it transforms the server's message
    into readable message for the user
    '''
    return connection.input.readline()[:-1]
