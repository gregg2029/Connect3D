from player import Player
from moves import *


class Game:
    # Create player dictionary. Key - Player id
    def player_init(self, num_players):
        player_name_dict = dict()
        for x in range(num_players):
            print("Enter name for player ", x+1, ":")
            player_name = str(input())
            player = Player(x, player_name)
            player_name_dict[x] = player

        return player_name_dict

    # Interpret move
    def interpret_move(self, move_str):
        move_str = move_str.upper().strip()
        str_arr = move_str.split(" ")
        keyword = str_arr[0]

        # Move switch statement
        move = None
        if keyword == "PLACE":
            if len(str_arr) > 1:
                arg_arr = str_arr[1:]
                move = Place(arg_arr)
            else:
                assert False, "Incorrect formatting"
        elif keyword == "PEEK":
            move = Peek()
        else:
            assert False, "Invalid move"

        return move
    
    def valid_location(self, rank, file):
        column = self.game_cube[rank][file]
        col_ind = -1
        for x in range(5):
            if column[x] == -1:
                col_ind = x
                break
        
        return rank, file, col_ind

    
    def place_helper(self, place):
        # Check if move is valid
        rank, file = Place.arguments(place)
        i, j, k = self.valid_location(rank, file)

        print(i, j, k)
        # Place player token in game cube

        # Update game status
    
    # Execute a move
    def execute_move(self, move):
        # Move switch statement
        if isinstance(move, Place):
            self.place_helper(move)
        elif isinstance(move, Peek):
            print("it is a peek move")
        else:
            assert False, "Invalid move"

    # End a turn
    def end_turn(self):
        self.turn += 1

    # Initialize a game
    def __init__(self):
        # Number of players
        print("Enter number of players:")
        num_players = int(input())
        self.num_players = num_players

        # Initialize players
        self.player_dict = Game.player_init(self, num_players)

        # Make game cube
        self.game_cube = [
            [[-1 for k in range(5)] for j in range(5)] for i in range(5)]

        self.turn = 1

        self.game_ended = False


# [
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]],
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]],
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]],
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]],
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# ]
