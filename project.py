import random
from abc import ABC, abstractmethod
from colorama import Fore, Style
import requests
import sys


class Character(ABC):
    """
    This is an abstract base class that defines the properties
    and methods shared by all characters in the game.
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        """Simulates the damage dealt in an attack."""
        pass

    def take_damage(self, damage):
        """Reduces health based on the damage received."""
        if self.health <= 0:
            raise ValueError("Game Over")
        self.health -= damage
        self.health = max(self.health, 0)

    def is_alive(self):
        """Returns True if the character has more than 0 health."""
        return self.health > 0

    def __str__(self):
        """Returns a string representation of the character."""
        return f"{self.name} has ❤️️{self.health} health points."


class Player(Character):
    """
    This class is the compound of all the properties
    and methods to manage a Player.
    """
    def __init__(self, name, health=100):
        super().__init__(name, health=health)

    def attack(self):
        """Simulates the damage the player deals in an attack."""
        return random.randint(5, 15)


class Enemy(Character):
    """
    This class has the methods and properties required to manage an Enemy.
    """
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        """Simulates the damage the enemy deals in an attack."""
        return random.randint(self.strength - 5, self.strength)


def main():
    """
    This Function manage the game logic.
    """
    print("Welcome to the Dungeon of Adventure!")
    player_name = input("What's your name, brave adventurer? ")
    player = Player(name=player_name)

    print_with_border(f"Welcome, {player.name.upper()}! Your adventure begins now...")
    print_with_border(
        "You are in a dark dungeon and must pass through " +
        "different rooms to find the exit."
    )

    try:
        while player.is_alive():
            event = generate_event()

            move_line = "Do you want to move to the next room? (y/n): "
            no_move_line = "You decide not to move forward and leave the dungeon."
            no_move_line += "See you in the next adventure!"
            move_forward = input(move_line).lower()
            defeat_line = "You have been defeated in the dungeon..."
            defeat_line += "Better luck next time!"
            normal_room = "Nothing happens in this room. You keep moving..."

            match event:
                case "battle":
                    enemy = generate_enemy()
                    battle(player, enemy)
                case "riddle":
                    solve_riddle(player)
                case "treasure":
                    show_image("image/treasure.png")
                    find_treasure(player)
                case "nothing":
                    print_with_border(normal_room)
                case _:
                    print("Unknown event!")

            print(player)  # Print player's health status
            
            if not player.is_alive():
                print(defeat_line)
                break
            print(f"Your health is {player.health}")
            
            if move_forward != 'y':
                print(no_move_line)
                break

        exit_line = "You have found the exit of the dungeon! Congratulations!"
        if player.is_alive():
            print_with_border(exit_line)
        else:
            print("GAME OVER.")
    finally:
        sys.exit("Error")

    print_with_border("Game Over!")


def generate_event():
    """Generates a random event: battle, riddle, treasure, or nothing"""
    events = ["battle", "riddle", "treasure", "nothing"]
    return random.choice(events)


def generate_enemy():
    """Generates a random enemy"""
    enemies = [
        Enemy("Orc", 50, 15),
        Enemy("Skeleton", 40, 12),
        Enemy("Goblin", 30, 10),
        Enemy("Dark Magician", 75, 20)
    ]
    return random.choice(enemies)


def battle(player, enemy):
    """Simulates a battle between the player and an enemy"""
    print_with_border(f"You are facing a {enemy.name}!")

    while enemy.is_alive() and player.is_alive():
        print(player)
        run_away_line = "Do you want to attack or run away? (attack/run): "
        action = input(run_away_line).lower()
        if action == "attack":
            player_damage = player.attack()
            enemy_damage = enemy.attack()
            
            enemy.take_damage(player_damage)
            player.take_damage(enemy_damage)

            print_with_border(f"You deal {player_damage} damage to the {enemy.name}.")
            print_with_border(f"The {enemy.name} deals {enemy_damage} damage to you.")
            
            if enemy.health <= 0:
                print_with_border(f"You have defeated the {enemy.name}!")
                break
            if not player.is_alive():
                print_with_border(
                    f"The {enemy.name} has defeated you...",
                    Fore.RED
                )
                break
        elif action == "run":
            success_run = random.choice([True, False])
            if success_run:
                print_with_border("You manage to escape the enemy!")
                break

            print_with_border("You can't escape, the enemy blocks your path.")
            enemy_damage = enemy.attack()
            player.take_damage(enemy_damage)
            print_with_border(f"The {enemy.name} attacks you and deals {enemy_damage} damage.")
        else:
            print("Invalid action. You must choose to either attack or run.")


def solve_riddle(player, answer=None):
    """Fetches a riddle from an API and evaluates the answer"""
    url = "https://opentdb.com/api.php?amount=1&type=boolean"
    response = requests.get(url, timeout=5)
    data = response.json()
    question = data['results'][0]['question']
    correct_answer = data['results'][0]['correct_answer']

    riddle_line = "You've encountered a magical riddle.\
    Solve it to be rewarded. Fail, and you'll be punished."
    print_with_border(riddle_line)
    
    if not answer:
        answer = input(f"Riddle: {question} (true/false): ").lower()

    if answer == correct_answer.lower():
        print_with_border("Correct! You receive a health reward.")
        player.health += random.randint(10, 30)
    else:
        print_with_border("Incorrect. You suffer a penalty.", Fore.RED)
        player.take_damage(random.randint(10, 20))
    return correct_answer.lower()


def find_treasure(player):
    """The player finds a treasure and recovers some health"""
    print_with_border("You found a treasure! You recover some health.")
    player.health += random.randint(10, 30)


def print_with_border(message, color=None):
    """
    Adding some fancy border to our messages.
    """
    border = "*" * (len(message) + 4)
    
    if not color:
        colors = [Fore.CYAN, Fore.GREEN, Fore.MAGENTA]
        border_color = random.choice(colors)
        message_color = random.choice(colors)
    else:
        border_color = color
        message_color = color
    border = border_color + "*" * (len(message) + 4) + Style.RESET_ALL
    print(border)
    print(message_color + f"* {message} *" + Style.RESET_ALL)
    print(border)


if __name__ == "__main__":
    main()
