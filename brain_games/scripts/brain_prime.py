#!/usr/bin/env puthon

from brain_games.games import brain_prime
from brain_games.engine_game import run_engine_game


def main():
    run_engine_game(brain_prime)


if __name__ == '__main__':
    main()
