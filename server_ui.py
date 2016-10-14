# Play connect four against Artificial Intelligence

import connect_server
import c4_shared_function
import connectfour

def play_game(connection: connect_server.GameConnection, game_state: connectfour.GameState):
    print('Welcome to AI Connect Four Game! In order to play the game, please type "DROP #" or "POP #" with # as the column that you want to drop or pop the piece!')
    print(c4_shared_function.board(game_state))
    
    
    while True:
        #This is printing out the user input and submitting the input to the server
        user_command = input()
        connect_server.input_user_command(connection, user_command)
        game_state = c4_shared_function.user_input(game_state, user_command)
        print(c4_shared_function.board(game_state))

        #This is getting the response from the server and printing it out
        response = connect_server.read_server_input(connection)
        
        print(response)
        if response == 'WINNER_RED' or 'WINNER_YELLOW':
            return
        elif response == 'INVALID':
            continue
        else:
            game_state = c4_shared_function.user_input(game_state, response)
            
        print(c4_shared_function.board(game_state))

    
def main():
    connection = connect_server.connect('woodhouse.ics.uci.edu', 4444)        
    
    username = input('What is your username? ')
    
    if connect_server.start_game(connection, username) == False:
        username = input('Invalid Username, please use another username: ')

    game_state = c4_shared_function.make_board()
    play_game(connection, game_state)

if __name__ == '__main__':
    main()
