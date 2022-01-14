
from tracemalloc import start
import snakeAndLadder

# Size of our board.
board_size = 10
total_snakes = 8
total_ladders = 8
dice_size = 6

# board getting initialised.
game_board = snakeAndLadder.Board(board_size, total_snakes, total_ladders,dice_size)

# Board designing.
game_board.board_designing()

# Placing snakes over board.
game_board.snake_positioning()

# Placing ladder over board.
game_board.ladder_positioning()

# Total number of player user want in this snake and ladder game.
total_player = int(input("Enter number of player you want to play : "))

#This is a hashmap of player and player represented by 1,2,3......
players = dict()
for num in range(1,total_player+1):
    player = snakeAndLadder.Player()
    players[player] = num

# Here the begins.
game_board.start_game(players)




