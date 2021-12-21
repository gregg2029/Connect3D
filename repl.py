from game_init.py import *

if __name__ == "__main__":
    print("Hello and welcome to Connect3D")
    print("Enter number of players")
    num_players = int(input())
    print(num_players)

    player_name_dict = player_init(num_players)
    print(player_name_dict)
