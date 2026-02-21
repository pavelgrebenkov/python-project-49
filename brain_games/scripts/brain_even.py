# brain_even.py
#!/usr/bin/env python3

from brain_games.games.cli import welcome_user
from brain_games.games import even
from brain_games.games.engine import run_game

def main():
    name = welcome_user()
    run_game(even, name)

if __name__ == '__main__':
    main()
