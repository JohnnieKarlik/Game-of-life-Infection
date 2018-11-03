import argparse

from board import Board
from game_rules import GOLStandardRules, GOLInfectionRules

    
class Game(object):
    """Game Of Life: Infection"""
    
    def __init__(self, width, height, infect_after, max_generations, seed):
        """"""
        self.width = width
        self.height = height
        self.infect_after = infect_after
        self.max_generations = max_generations
        self.seed = seed
        self.board = Board(width, height, seed)
    
    def evolve(self, strategy):
        """evolve single step"""
        for row in xrange(self.height):
            for col in xrange(self.width):
                is_alive = self.board.is_alive(row, col)
                neibors_count = self.board.count_neigbors(row, col, strategy.get_count_type(is_alive))
                next_state = strategy.get_next_state(is_alive, neibors_count)
                self.board.set_next_state(row, col, next_state)
        
        self.board.update_board()
        print self.board

    def play(self):
        """run GOL"""
        standard_rules = GOLStandardRules()
        infection_rules = GOLInfectionRules()
        
        print self.board
        strategy = standard_rules
        curr_generation = 0
        while curr_generation < self.max_generations:
            if curr_generation == self.infect_after:
                strategy = infection_rules
            self.evolve(strategy)
            curr_generation += 1


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--infect_after', type=int)
    parser.add_argument('--max_generations', type=int)
    parser.add_argument('--seed')
    args = parser.parse_args()
    
    game = Game(args.width, args.height, args.infect_after, args.max_generations, args.seed)
    game.play()