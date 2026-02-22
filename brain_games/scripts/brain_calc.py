# brain_calc.py
#!/usr/bin/env python3

from brain_games.games.cli import welcome_user
from brain_games.games import calc
from brain_games.games.engine import run_game

def main():
    name = welcome_user()
    run_game(calc, name)

if __name__ == '__main__':
    main()
