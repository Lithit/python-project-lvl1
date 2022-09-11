#1/usr/bin/env python

from brain_games.games import brain_even
from brain_games.engine_game import get_engine_game


def main():
    get_engine_game(brain_even)


    if __name__ == '__main__':
        main()
