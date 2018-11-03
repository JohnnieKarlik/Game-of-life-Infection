import unittest

from board import Board
from game_rules import GOLStandardRules, GOLInfectionRules


class BoardTestCases(unittest.TestCase):

    def test_board_height(self):
        width = 3
        height = 4
        seed = '0 0 0 0 0 0 0 0 0 0 0 0'
        board = Board(width, height, seed)
        
        self.assertEqual(board.height, height, 'incorrect board height')
        self.assertEqual(len(board.curr_state_board), height, 'incorrect board height')
        
    def test_board_width(self):
        width = 3
        height = 4
        seed = '0 0 0 0 0 0 0 0 0 0 0 0'
        board = Board(width, height, seed)
        
        self.assertEqual(board.width, width, 'incorrect board width')
        self.assertEqual(len(board.curr_state_board[0]), width, 'incorrect board width')
        
    def test_board_init(self):
        width = 2
        height = 2
        seed = '0 1 0 1'
        board = Board(width, height, seed)
        
        self.assertFalse(board.is_alive(0, 0))
        self.assertFalse(board.is_alive(1, 0))
        self.assertTrue(board.is_alive(0, 1))
        self.assertTrue(board.is_alive(1, 1))
        
    def test_board_update(self):
        width = 2
        height = 2
        seed = '0 1 0 1'
        board = Board(width, height, seed)
        
        board.next_state_board = [[True, False], [True, False]]
        board.update_board()
        
        self.assertTrue(board.is_alive(0, 0))
        self.assertTrue(board.is_alive(1, 0))
        self.assertFalse(board.is_alive(0, 1))
        self.assertFalse(board.is_alive(1, 1))

    def test_board_print(self):
        width = 2
        height = 2
        seed = '0 1 0 1'
        board = Board(width, height, seed)
        self.assertEqual(str(board), seed)
        
    def test_board_count_neigbors(self):
        width = 3
        height = 4
        seed = '''1 1 1 0 1 1 1 1 1 0 0 1'''
        board = Board(width, height, seed)
        
        self.assertEqual(board.count_neigbors(0, 0, 'hor_ver'), 3)
        self.assertEqual(board.count_neigbors(0, 0, 'arround'), 2)

        self.assertEqual(board.count_neigbors(0, 1, 'hor_ver'), 4)
        self.assertEqual(board.count_neigbors(0, 1, 'arround'), 4)

        self.assertEqual(board.count_neigbors(0, 2, 'hor_ver'), 5)
        self.assertEqual(board.count_neigbors(0, 2, 'arround'), 3)
        
        self.assertEqual(board.count_neigbors(1, 0, 'hor_ver'), 4)
        self.assertEqual(board.count_neigbors(1, 0, 'arround'), 5)

        self.assertEqual(board.count_neigbors(1, 1, 'hor_ver'), 3)
        self.assertEqual(board.count_neigbors(1, 1, 'arround'), 7)

        self.assertEqual(board.count_neigbors(1, 2, 'hor_ver'), 4)
        self.assertEqual(board.count_neigbors(1, 2, 'arround'), 5)

        self.assertEqual(board.count_neigbors(2, 0, 'hor_ver'), 3)
        self.assertEqual(board.count_neigbors(2, 0, 'arround'), 2)
        
        self.assertEqual(board.count_neigbors(2, 1, 'hor_ver'), 4)
        self.assertEqual(board.count_neigbors(2, 1, 'arround'), 5)        

        self.assertEqual(board.count_neigbors(2, 2, 'hor_ver'), 5)
        self.assertEqual(board.count_neigbors(2, 2, 'arround'), 4)        
        
        self.assertEqual(board.count_neigbors(3, 0, 'hor_ver'), 3)
        self.assertEqual(board.count_neigbors(3, 0, 'arround'), 2)
        
        self.assertEqual(board.count_neigbors(3, 1, 'hor_ver'), 4)
        self.assertEqual(board.count_neigbors(3, 1, 'arround'), 4)        

        self.assertEqual(board.count_neigbors(3, 2, 'hor_ver'), 3)
        self.assertEqual(board.count_neigbors(3, 2, 'arround'), 2)        


class RulesTestCases(unittest.TestCase):
    
    def test_standard_rules_count_type(self):
        rules = GOLStandardRules()
        self.assertEqual(rules.get_count_type(is_alive=True), 'arround', 'incorrect count type')
        self.assertEqual(rules.get_count_type(is_alive=False), 'arround', 'incorrect count type')
    
    def test_infection_rules_count_type(self):
        rules = GOLInfectionRules()
        self.assertEqual(rules.get_count_type(is_alive=True), 'hor_ver', 'incorrect count type')
        self.assertEqual(rules.get_count_type(is_alive=False), 'arround', 'incorrect count type')
  
    def test_standard_rules_get_next_state(self):
        rules = GOLStandardRules()
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=0))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=1))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=2))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=3))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=4))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=5))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=6))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=7))
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=8))
        
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=0))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=1))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=2))
        self.assertTrue(rules.get_next_state(is_alive=False, neigbors_count=3))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=4))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=5))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=6))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=7))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=8))
    
    def test_infection_rules_get_next_state(self):
        rules = GOLInfectionRules()
        self.assertFalse(rules.get_next_state(is_alive=True, neigbors_count=0))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=1))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=2))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=3))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=4))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=5))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=6))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=7))
        self.assertTrue(rules.get_next_state(is_alive=True, neigbors_count=8))
        
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=0))
        self.assertTrue(rules.get_next_state(is_alive=False, neigbors_count=1))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=2))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=3))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=4))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=5))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=6))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=7))
        self.assertFalse(rules.get_next_state(is_alive=False, neigbors_count=8))
    

if __name__ == '__main__':
    unittest.main()
