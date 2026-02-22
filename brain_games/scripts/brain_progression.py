# brain_progression.py
# !/usr/bin/env python3

from brain_games.games.cli import welcome_user
from brain_games.games import progression
from brain_games.games.engine import run_game


def main():
    name = welcome_user()
    run_game(progression, name)


if __name__ == '__main__':
    main()
