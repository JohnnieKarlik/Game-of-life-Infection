from collections import namedtuple
from game_rules import Rules

from copy import deepcopy 

class Board(object):
    
    def __init__(self, width, height, seed):
        """set game board with seed"""
        self.height = height
        self.width = width
        self.curr_state_board = self.__create_board(seed, width)
        self.next_state_board = self.__create_board(seed, width)
        pass
    
    def __create_board(self, seed, width):
        """one dimentional array to two dimentional array"""
        to_cells = [bool(int(item)) for item in seed.split(' ')]
        to_two_dim = [to_cells[i:i+width] for i in range(0, len(to_cells), width)]
        return to_two_dim
    
    def __str__(self):
        """flatten two dim array into space seperated string"""
        return ' '.join(str(int(cell)) 
                        for row 
                        in self.curr_state_board 
                            for cell 
                            in row)
        
        ## debug, print as matrix 
        #re = ''
        #for i in self.curr_state_board:
            #for j in i:
                #re += str(int(j)) + ' '
            #re += '\n'
        #return re
    
    def update_board(self):
        """update next-state > curr-state """
        self.curr_state_board = deepcopy(self.next_state_board)

    def is_alive(self, row, col):
        return self.curr_state_board[row][col]
    
    def set_next_state(self, row, col, is_alive):
        self.next_state_board[row][col] = is_alive

    def count_neigbors(self, row, col, count_type):
        """count neighbors according to policy"""
        neigbor_count = 0
        
        if count_type == Rules.count_type_arround:
            neigbor_count = self._count_neighbors_arround_cell(row, col)
                    
        elif count_type == Rules.count_type_hor_ver:   
            neigbor_count = self._count_neighbors_hor_ver(row, col)

        return neigbor_count;
    
    def _count_neighbors_arround_cell(self, row, col):
        """count arround live neighbors"""
        neigbor_count = 0
        
        # Check cell on the bottom.
        if row != (self.height - 1):
            if self.curr_state_board[row + 1][col]:
                neigbor_count += 1
        
        # Check cell on the bottomw right.
        if row != (self.height - 1) and col != (self.width - 1):
            if self.curr_state_board[row + 1][col + 1]:
                neigbor_count += 1
        
        # Check cell on the right.
        if col != (self.width - 1):
            if self.curr_state_board[row][col + 1]:
                neigbor_count += 1
        
        # Check cell on the bottom left.
        if row != 0 and col != (self.width - 1):
            if self.curr_state_board[row - 1][col + 1]:
                neigbor_count += 1
        
        # Check cell on the left.
        if row != 0:
            if self.curr_state_board[row - 1][col]:
                neigbor_count += 1
        
        # Check cell on the top left.
        if row != 0 and col != 0:
            if self.curr_state_board[row - 1][col - 1]:
                neigbor_count += 1
        
        # Check cell on the top.
        if col != 0:
            if self.curr_state_board[row][col - 1]:
                neigbor_count += 1
        
        # Check cell on the top right.
        if row != (self.height - 1) and col != 0:
            if self.curr_state_board[row + 1][col - 1]:
                neigbor_count += 1
                
        return neigbor_count
    
    def _count_neighbors_hor_ver(self, row, col):
        """count horizontal or vertical live neighbors """
        row_count = sum(cell 
                        for i, cell 
                        in enumerate(self.curr_state_board[row]) 
                        if i != col)
        
        col_count = sum(cell
                        for idx, cell 
                        in enumerate(self.curr_state_board[i][col] 
                                     for i 
                                     in range(self.height)) 
                        if idx != row)

        return row_count + col_count