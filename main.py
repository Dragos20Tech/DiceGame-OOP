import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):  # READ-ONLY
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    # READ-ONLY
    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("===========================")
        print("Welcome to Roll the Dice!")
        print("===========================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner & loser
        if player_value > computer_value:
            print("You won the round!")
            self.update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("Mission failed... We'll get'em next time!")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie! ")

        # Show counters
        self.show_counters()

    def print_round_welcome(self):
        print("\n------- New Round -------")
        input("Press any key to roll the dice!")

    def show_dice(self, player_value, computer_value):
        print(f"\nYour die : {player_value}")
        print(f"Computer die : {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter : {self._player.counter}")
        print(f"Computer counter : {self._computer.counter}\n")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n====================")
            print("G A M E   O V E R ")
            print("====================")
            print("Computer won the game. See you next time!")
            print("===========================================")
        else:
            print("\n====================")
            print("G A M E   O V E R ")
            print("====================")
            print("You won the game! Well done!")
            print("===========================================")


player_die = Die()
computer_die = Die()

player = Player(player_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)

# Start the game

game.play()