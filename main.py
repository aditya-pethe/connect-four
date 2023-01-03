from sys import argv
import connect4
import argparse
import random
import os

game = connect4.connect4()

print("_______START GAME!________")

game.print_board()

game_state = "undecided"

while True:

    column = int(input('Enter the column you would like to place\n'))
    game.place(column)
    game.print_board()

    if game.check_if_win():
        break

    game.switch_turn()






