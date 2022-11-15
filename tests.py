import unittest
import logic

class TestLogic(unittest.TestCase):
    def test_Game_get_winner(self):
        game = logic.Game()
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board1 = [
            ['O', 'O', 'O'],
            ['X', 'X', None],
            [None, 'O', 'X'],
        ]
        board2 = [
            ['X', None, 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        board3 = [
            ['O', None, 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(game.get_winner(board), 'X')
        self.assertEqual(game.get_winner(board1), 'O')
        self.assertEqual(game.get_winner(board2), None)
        self.assertEqual(game.get_winner(board3), 'X')
    
    def test_Game_other_player(self):
        game = logic.Game()
        self.assertEquals(game.other_player('O'),'X')
        self.assertEquals(game.other_player('X'),'O')
    
    def test_People_input_position(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        human1 = logic.People("O")
        human2 = logic.People("X")
        human1.board = board
        board_after = [
            ['X', 'O', 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(human1.input_position("(1,2)"),board_after)
        
if __name__ == '__main__':
    unittest.main()