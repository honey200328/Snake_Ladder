import random


class SnakeAndLadder:
    def __init__(self, num_snakes, num_ladders):
        self.players = {}  # Tracks player positions
        self.snakes = {}  # Initialize snakes before generating them
        self.ladders = {}  # Initialize ladders before generating them
        self.snakes = self.generate_snakes_or_ladders(num_snakes, "snake")
        self.ladders = self.generate_snakes_or_ladders(num_ladders, "ladder")
        self.winner = None

    def generate_snakes_or_ladders(self, count, type_):
        positions = {}
        while len(positions) < count:
            start = random.randint(2, 99)
            if type_ == "snake":
                end = random.randint(1, start - 1)  # Snakes go down
            elif type_ == "ladder":
                end = random.randint(start + 1, 100)  # Ladders go up
            if start not in positions and start not in self.snakes and start not in self.ladders:
                positions[start] = end
        return positions

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, dice_value):
        current_position = self.players[player]
        new_position = current_position + dice_value

        if new_position > 100:  # Exceeds board limit
            print(f"{player} rolled {dice_value}, but cannot move. Current position: {current_position}.")
            return current_position

        # Check for snakes or ladders
        if new_position in self.snakes:
            print(f"{player} encountered a snake at {new_position}! Sliding down to {self.snakes[new_position]}.")
            new_position = self.snakes[new_position]
        elif new_position in self.ladders:
            print(f"{player} found a ladder at {new_position}! Climbing up to {self.ladders[new_position]}.")
            new_position = self.ladders[new_position]

        print(f"{player} moved from {current_position} to {new_position}.")
        return new_position

    def play_turn(self, player):
        input(f"{player}, press Enter to roll the dice...")  # Wait for player to roll the dice
        dice_value = self.roll_dice()
        print(f"{player} rolled a {dice_value}.")
        self.players[player] = self.move_player(player, dice_value)

        if self.players[player] == 100:
            self.winner = player
            print(f"🎉 Congratulations! {player} has won the game!")
            return True
        return False

    def start_game(self):
        print("Starting Snake and Ladder Game!")
        print(f"Snakes: {self.snakes}")
        print(f"Ladders: {self.ladders}")
        print("Players: ", list(self.players.keys()))

        player_list = list(self.players.keys())
        turn = 0

        while not self.winner:
            current_player = player_list[turn]
            game_over = self.play_turn(current_player)
            if game_over:
                break

            # Move to the next player
            turn = (turn + 1) % len(player_list)


# Initialize the game
num_players = int(input("Enter the number of players: "))
players = [input(f"Enter name of Player {i + 1}: ") for i in range(num_players)]

num_snakes = int(input("Enter the number of snakes: "))
num_ladders = int(input("Enter the number of ladders: "))

# Create the game instance
game = SnakeAndLadder(num_snakes, num_ladders)

# Add players to the game dynamically
for player in players:
    game.players[player] = 0  # All players start at position 0

# Start the game
game.start_game()