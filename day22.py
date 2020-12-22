from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 10)

data_file_name = "inputs/day22"
testing_file_name = data_file_name + "_test"

def get_score(deck):
    return sum(v * (len(deck) - i) for i, v in enumerate(deck))

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        playertexts = file.read().split("\n\n")
        decks = [[int(l) for l in pt.split("\n")[1:]] for pt in playertexts]

        while not any(len(deck) == 0 for deck in decks):
            cards = [deck[0] for deck in decks]
            best_card = max(cards)
            winner_index = cards.index(best_card)
            decks = [deck[1:] if i != winner_index else deck[1:] + sorted(cards, reverse=True) for i, deck in enumerate(decks)]

        print([get_score(deck) for deck in decks])

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        playertexts = file.read().split("\n\n")
        decks = [[int(l) for l in pt.split("\n")[1:]] for pt in playertexts]


        def play(decks, depth = 0):
            deck_history = set()
            round = 1
            while not any(len(deck) == 0 for deck in decks):
                #print(f"depth {depth}, round {round}")
                #print(decks)
                game_id = tuple(get_score(deck) for deck in decks)
                if game_id in deck_history:
                    #print("immediate fail")
                    return (True, decks)
                deck_history.add(game_id)
                
                cards = [deck[0] for deck in decks]
                winner_index = 0
                if not all(card < len(deck) for card, deck in zip(cards, decks)):
                    best_card = max(cards)
                    winner_index = cards.index(best_card)
                else:
                    sub_decks = [deck[1:card + 1] for card, deck in zip(cards, decks)]
                    immediate, result_decks = play(sub_decks, depth + 1)
                    
                    winner_index = 0 if (immediate or len(result_decks[0]) != 0) else 1
                                
                decks = [deck[1:] if i != winner_index else deck[1:] + [cards[winner_index]] + [cards[1 - winner_index]] for i, deck in enumerate(decks)]
                round += 1
            
            return (False, decks)


        _, final_decks = play(decks)
        print([get_score(deck) for deck in final_decks])

        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)