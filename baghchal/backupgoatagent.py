from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class backupGoatAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(backupGoatAgent, self).__init__(game,side)
        if side != Const.MARK_GOAT:
            raise ValueError("side must be goat")

        #idea = if tiger has ability to capture, goat fills spot where tiger will land after 
        #capping the goat

    def propose(self) -> Move:
        moves = self.game.goatMoves()
        for move in moves:
            if move.capture:
                return move
        return random.choice(moves)
