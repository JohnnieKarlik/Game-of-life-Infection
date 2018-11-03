from abc import ABCMeta, abstractmethod


class Rules(object):
    __metaclass__ = ABCMeta
    
    count_type_hor_ver = 'hor_ver'
    count_type_arround = 'arround'
    
    @abstractmethod
    def get_next_state(self, is_alive, neigbors_count):
        pass
    
    @abstractmethod
    def get_count_type(self, is_alive):
        pass


class GOLStandardRules(Rules):
    """ 1. Any live cell with fewer than two live neighbors dies (under population).
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies (overpopulation).
        4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)."""

    def get_next_state(self, is_alive, neigbors_count):
        if is_alive == True: 
            if neigbors_count <= 1:
                return False
            elif 2 <= neigbors_count <= 3:
                return True
            else:
                return False
            
        else:
            if neigbors_count == 3:
                return True
        
        return False

    def get_count_type(self, is_alive):
        return Rules.count_type_arround


class GOLInfectionRules(Rules):
    """ 1. Any dead cell with a single live neighbor lives on to the next generation.
        2. Any live cell with no horizontal or vertical live neighbors dies."""
    
    def get_next_state(self, is_alive, neigbors_count):
        if is_alive and neigbors_count == 0:
            return False
        elif not is_alive and neigbors_count == 1:
            return True
        else:
            return is_alive
    
    def get_count_type(self, is_alive):
        if is_alive:
            return Rules.count_type_hor_ver
        else:
            return Rules.count_type_arround        