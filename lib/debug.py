#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result


# __name__ --> the name of the module that things are happening
# when __name__ == '__main__' it will only run the additionally code if we're running the file directly

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    p1 = Player(username="Player One")
    p2 = Player(username="Player Two")
    p3 = Player(username="skibidi_t")

    g1 = Game(title="Galaga")
    g2 = Game(title="Ms. PacMan")

    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r1 = Result(player=p1, game=g1, score=1234)
    r2 = Result(player=p2, game=g1, score=4321)
    r3 = Result(player=p2, game=g2, score=670)
    r4 = Result(player=p2, game=g1, score=999)
    r5 = Result(player=p1, game=g2, score=80)

    ipdb.set_trace()
