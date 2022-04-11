#!/usr/bin/env puthon

from brain_games.games import brain_gcd
from brain_games.engine_game import get_engine_game


def main():
    get_engine_game(brain_gcd)


    if __name__ == '__main__':
        main()
