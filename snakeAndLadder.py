import random


class Board:
    def __init__(self, board_size=10, snakes=8, ladders=8, dice_size=6):
        # Board created position indexed from 1.
        self.board_size = board_size
        self.board = []
        self.total_snake = snakes
        self.total_ladder = ladders
        self.winner = board_size * board_size  # maximum value of the board after reaching this value player will win.
        self.ladders_position = dict()  # key as a ladder bottom and value as ladder top.
        self.snakes_position = dict()  # key as a snake mouth and value as snake tail.
        self.dice_size = dice_size  # maximum value of our dice.

    # Board get filled by values.
    def board_designing(self):
        # Board is initializes with value 1
        values = 1

        # filling up the board from 1 to square of board size.
        for row in range(self.board_size):
            col_matrix = []
            for col in range(self.board_size):
                col_matrix.append(values)
                values += 1
            self.board.append(col_matrix)

    # Snakes placed in board and also give option to users to placed ladder as per their own choiced positions
    def snake_positioning(self):
        print("Reply either 0 or 1")

        while True:
            is_userdesigning = int(input("Do you want to put snakes as per wish ?"))

            if is_userdesigning == 1:
                user_wanted_snakes = int(input("Enter how many snakes you want in this game : "))
                self.total_snake = user_wanted_snakes
                snakes_count = 1
                is_all_snakes_filled = False

                while snakes_count <= self.total_snake:
                    head = int(input("Enter value at which snake {} head present : ".format(snakes_count)))
                    tail = int(input("Enter value at which snake {} tail present: ".format(snakes_count)))

                    # head and tail position are out of the board then re-enter their positions.
                    if head < self.winner and tail < self.winner and head > tail:
                        self.snakes_position[head] = tail
                        snakes_count += 1
                    else:
                        print("Re-enter head and tail of snake {}".format(snakes_count))

                    # If user enter position of all the snakes then snake position filling breaks.
                    if snakes_count == self.total_snake + 1:
                        is_all_snakes_filled = True
                        break
            elif is_userdesigning == 0:
                self.snakes_position = {98: 79, 95: 75, 93: 73, 87: 36, 64: 60, 62: 19, 54: 34, 17: 7}
                break
            else:
                print("You haven't choose 0 or 1 please choose either of them")

            if is_all_snakes_filled:
                break

    # Ladder placed in board by default and give option the users too.
    def ladder_positioning(self):
        print("Answer 1 or 0 only")

        while True:
            isuserdesigning = int(input("Do you want to put ladder by your own ?"))

            if isuserdesigning == 1:
                user_wanted_ladder = int(input("Enter total ladder you want for this game: "))
                self.total_ladder = user_wanted_ladder
                ladders_count = 1
                is_all_ladder_filled = False

                while ladders_count <= self.total_ladder:
                    ladder_start = int(input("Enter start of ladder {} : ".format(ladders_count)))
                    ladder_end = int(input("Enter end of ladder {} : ".format(ladders_count)))

                    if ladder_start < self.winner and ladder_end < self.winner and ladder_start < ladder_end:
                        ladders_count += 1
                        self.ladders_position[ladder_start] = ladder_end
                    else:
                        print("Re-enter ladder {} start and end".format(ladders_count))

                    # user entered all position of the ladder then we break.
                    if ladders_count == self.total_ladder + 1:
                        is_all_ladder_filled = True
                        break

            elif isuserdesigning == 0:
                self.ladders_position = {2: 23, 5: 13, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
                break
            else:
                print("You haven't choose 0 or 1 please choose either of them")

            if is_all_ladder_filled:
                break

    # Dice throw is perform here.
    def dice(self):
        # each time new number generate including 1 and size.
        return random.randint(1, self.dice_size)

    # This method help players to decide who won and who loose.
    def start_game(self, players):
        winner_players = dict()

        while True:

            for player in players:
                if player not in winner_players:
                    # output of dice get added to players current position and we apply some codition over next position.
                    next_position = player.position + self.dice()

                    if next_position == 100:  # This player is a winner.
                        winner_players[player] = 1
                        print("Hurray Player {} win the game".format(players[player]))
                        # if len(players) - len(winner_players) == 1:
                        #     print("Player {} lost the game".format(self.get_looser(winner_players,players)))
                        #     break
                    elif next_position < 100:  # respective player position is less than 100 means he/she can throw more dice.

                        # checking whether player at snake mouth or not.
                        if next_position in self.snakes_position:
                            player.position = self.snakes_position[next_position]
                        else:
                            player.position = next_position

                        # checking whether player at bottom of ladder or what.
                        if next_position in self.ladders_position:
                            player.position = self.ladders_position[next_position]
                        else:
                            player.position = next_position

            if len(players) - len(winner_players) == 1:
                print("Player {} lost the game".format(self.get_looser(winner_players, players)))
                break

    # Return the player who looses this snake and ladder game.
    def get_looser(self, winner_players, total_players):

        for player in total_players:
            if player not in winner_players:
                return total_players[player]


# Player class and initialized player at position 1.
class Player:
    def __init__(self) -> None:
        self.position = 1












