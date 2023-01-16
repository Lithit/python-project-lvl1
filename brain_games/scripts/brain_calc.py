#!/usr/bin/env python

from brain_games.games import brain_calc
from brain_games.engine_game import run_engine_game


def main():
    run_engine_game(brain_calc)


if __name__ == '__main__':
    main()
