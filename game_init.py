def player_init(num_players):
    player_name_dict = dict()
    for x in range(num_players):
        print("Enter name for player ", x, ":")
        player_name_dict[x] = str(input())

    return player_name_dict
