#!/usr/bin/env python3

from brain_games.games.cli import welcome_user
from brain_games.games.brain_calc_code import comp_decision


def main():
    name = welcome_user()
    comp_decision(name)


if __name__ == '__main__':
    main()
