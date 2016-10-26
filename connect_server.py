# James Anh Minh Nguyen ID: 45298461    Kammy Deng ID: 72943066
#
# This module connects with server and creates the protocol to communicate
# with the server
# This includes functions that connects to the server, varifys the username,
# reads the lines from the server, sends the lines to the server, and closes
# the connection.


from collections import namedtuple
import socket

GameConnection = namedtuple(
    'GameConnection',
    ['socket', 'input', 'output'])


def connect(host: str, port: int) -> GameConnection:
    '''
    Connects to the identified host and port, writes
    the user input into a readable message for the server,
    reads from the server's output, and return the socket,
    input, output as a namedtuple.
    '''
    game_socket = socket.socket()
    game_socket.connect((host, port))

    game_input = game_socket.makefile('r')
    game_output = game_socket.makefile('w')

    return GameConnection(game_socket, game_input, game_output)


def start_connection(connection: GameConnection, username: str) -> bool:
    '''
    Starts the game with an username. If the username is valid
    returns True. If not, returns False and closes the connection.
    Return None if the server doesn't work.
    '''
    try:
        command = 'I32CFSP_HELLO ' + username
        _write_line(connection, command)
        first_response = _read_line(connection)

        if first_response == 'WELCOME ' + username:
            _write_line(connection, 'AI_GAME')
            second_response = _read_line(connection)

            if second_response == 'READY':
                return True
            else:
                close(connection)
                return

        elif first_response == 'ERROR':
            return False

        
    except Exception as E:
        print(E)
        close(connection)
        return


def input_user_command(connection: GameConnection, user_command: str) -> None:
    '''
    Input the user command into the server
    '''
    _write_line(connection, user_command)


def read_server_input(connection: GameConnection):
    '''
    Interpret the input from server, make sure the server is writing the right command.
    If not, close the connection. If the input is correct, return a list of responses.
    '''
    try:
        first_response = _read_line(connection)

        if first_response == 'OKAY':
            second_response = _read_line(connection)
            third_response = _read_line(connection)

            if third_response == 'READY' or 'WINNER_YELLOW':
                result = [second_response, third_response]
            else:
                close(connection)
                print('SERVER CRASHED')

        elif first_response == 'WINNER_RED':
            result = [first_response]

        elif first_response == 'INVALID':
            second_response = _read_line(connection)
            if second_response == 'READY':
                result = [first_response, second_response]
            else:
                print('SERVER CRASHED')
                close(connection)

    except Exception as Error:
        print(Error)

    finally:
        return result


def close(connection: GameConnection) -> None:
    '''
    It closes all the connection with the server
    '''
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def _write_line(connection: GameConnection, command: str) -> None:
    '''
    From the identified connection, it transforms user input
    into certain message for the server and flushes it out.
    '''
    connection.output.write(command + '\r\n')
    connection.output.flush()


def _read_line(connection: GameConnection) -> str:
    '''
    From the identified connection, it reads the server's message for the user
    '''
    return connection.input.readline()[:-1]
