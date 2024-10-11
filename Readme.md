# Adventure Game

Welcome to the Adventure Game project! This is a simple text-based game where players can battle enemies by solving puzzles. The game features character classes, abstract base classes, and a fun interactive experience.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Gameplay](#gameplay)
- [Classes](#classes)
- [Requirements](#requirements)
- [License](#license)

## Features

- Player and Enemy classes that inherit from an abstract base class.
- Randomized damage calculations for attacks.
- A simple user interface for battling enemies and solving puzzles.

## Getting Started

To get started with the Adventure Game, clone this repository to your local machine:

```bash
git clone https://github.com/nataliac/adventure-game.git
cd adventure-game
pip install requirements.txt

Gameplay

In this game, you will assume the role of a player who faces different enemies. Each turn, you can choose to attack the enemy. The goal is to defeat all enemies while managing your health.
How to Play

    Start the game.
    Choose to attack the enemy.
    Monitor your health and the enemy's health.
    Win by defeating the enemy!

Classes
Character (Abstract Base Class)

    Properties:
        name: The name of the character.
        health: The health points of the character.

    Methods:
        attack(): Abstract method to be implemented by subclasses.
        take_damage(damage): Reduces the health based on the damage received.
        is_alive(): Returns True if the character has health remaining.
        __str__(): Returns a string representation of the character.

Player

Inherits from Character and represents the player in the game.

    Methods:
        attack(): Simulates damage dealt by the player.

Enemy

Inherits from Character and represents an enemy character.

    Properties:
        strength: The strength used to calculate damage dealt.

    Methods:
        attack(): Simulates damage dealt by the enemy.

Requirements

    Python 3.x
    Any additional libraries (if applicable)

License

Final Project for CS50 - Python - [License](https://cs50.harvard.edu/python/2022/license/)
