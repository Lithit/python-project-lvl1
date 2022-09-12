#!/usr/bin/env python

from brain_games.games import brain_progression
from brain_games.engine_game import get_engine_game


def main():
    get_engine_game(brain_progression)


if __name__ == '__main__':
    main()
