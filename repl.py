from game_init import Game


if __name__ == "__main__":
    print("Hello and welcome to Connect3D!")
    # Create game
    game = Game()

    while not game.game_ended:
        turn_num = game.turn
        player_id = (turn_num-1) % game.num_players
        player = game.player_dict[player_id]
        print("Turn ", game.turn, ", ", player.name, "'s move:")
        move = str(input())

        Game.end_turn(game)