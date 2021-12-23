from game import Game


if __name__ == "__main__":
    print("Hello and welcome to Connect3D!")
    # Create game
    game = Game()

    while not game.game_ended:
        # Determine whose move it is
        turn_num = game.turn
        player_id = (turn_num-1) % game.num_players
        player = game.player_dict[player_id]

        # Prompt player for move and interpret
        print("Turn ", game.turn, ", ", player.name, "'s move:")
        move = game.interpret_move(str(input()))

        # Execute move
        game.execute_move(move)

        # Update state as needed to end turn
        Game.end_turn(game)


'''
          ______________________________
         /     /     /     /     /     /
        /_____/_____/_____/_____/_____/
       /     /     /     /     /     /
      /_____/_____/_____/_____/_____/
     /     /     /     /     /     /
    /_____/_____/_____/_____/_____/
   /     /     /     /     /     /
  /_____/_____/_____/_____/_____/
 /|    /|    /|    /|    /|    /
/_|___/_|___/_|___/_|___/_|___/
| |___|_|___|_|___|_|___|_|___|
| /   | /   | /   | /   | /   |
|/____|/____|/____|/____|/____|
|     |     |     |     |     |
|     |     |     |     |     |
|_____|_____|_____|_____|_____|
|     |     |     |     |     |
|     |     |     |     |     |
|_____|_____|_____|_____|_____|
|     |     |     |     |     |
|     |     |     |     |     |
|_____|_____|_____|_____|_____|
|     |     |     |     |     |
|     |     |     |     |  0  |
|_____|_____|_____|_____|_____|
'''
