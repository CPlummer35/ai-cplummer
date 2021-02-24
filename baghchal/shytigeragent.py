#shy tiger
from typing import List, Tuple, Optional
from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class ShyTigerAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(ShyTigerAgent, self).__init__(game,side)
        if side != Const.MARK_TIGER:
            raise ValueError("side must be tiger")
    def isCloseToGoat(self,row : int, col : int):
        game : Game = self.game
        board : List[List[int]] = game.board
        for (dRow,dCol) in Const.DIRS[(row,col)]:
            if board[row+dRow][col+dCol] == Const.MARK_GOAT:
                return True
        return False

    def propose(self) -> Move:
        notCloseToGoatMoves : List[Move] =  []
        moves = self.game.tigerMoves()
        for move in moves:
            if not self.isCloseToGoat(move.toRow,move.toCol):
                notCloseToGoatMoves.append(move)
        if len(notCloseToGoatMoves) > 0:
            return random.choice(notCloseToGoatMoves)
        if (len(moves) == 0):
            print(self.game)
        return random.choice(moves)
