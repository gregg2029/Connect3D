from player import Player


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
        self.game_cube = [[[-1 for k in range(5)] for j in range(5)] for i in range(5)]

        self.turn = 1

        self.game_ended = False


# [
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]], 
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]], 
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]], 
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]], 
# [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# ]