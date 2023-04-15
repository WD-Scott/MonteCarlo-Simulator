import unittest
from montecarlo import Die, Game, Analyzer
import pandas as pd
import numpy as np
import pandas.testing as pdt

class MonteCarloTestSuit(unittest.TestCase):
    '''
    Test suite for methods and return outputs
    '''
    
    def test_die(self):
        '''
        Tests weight creation.
        '''        
        die = Die([1,2,3,4,5,6])
        x = 1
        if x not in die.faces_weights['Weights'].values:
            raise AssertionError
        
            
    def test_weight_change(self):
        '''
        Tests the weight_changed method.
        '''        
        die = Die([1,2,3,4,5,6])
        die.change_weight(3,5)
        expected = 5
        actual = die.show_die().loc[die.show_die()['Faces'] == 3, 'Weights'].values[0]
        self.assertEqual(expected, actual)
        
        
    def test_rolls(self):
        '''
        Tests the rolls method.
        '''
        die = [1,2,3,4,5,6]
        test_3 = Die(die)
        roll = test_3.rolls(3)
        self.assertEqual(len(roll), 3)
        
        
    def test_show(self):
        '''
        Tests the show_faces_weights method.
        '''
        die = [1,2,3,4,5,6]
        test_4 = Die(die)
        test_4_df = test_4.show_die()
        test_4_type = type(test_4_df)
        x = pd.DataFrame()
        pd_type = type(x)
        self.assertEqual(test_4_type, pd_type)
     
    
    def test_gameplay(self):
        '''
        Tests the play method.
        '''
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        expect_row = 100
        actual_row = game.show_play().shape[0]
        self.assertEqual(expect_row, actual_row)
        expect_col = 3
        actual_col = game.show_play().shape[1]
        self.assertEqual(expect_col, actual_col)
        

    def test_show2(self):
        '''
        Tests the show method for narrow form.
        '''        
        game = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
        game.play(100)
        expect_row = 300
        actual_row = game.show_play(form='narrow').shape[0]
        self.assertEqual(expect_row, actual_row)
        expect_col = 1
        actual_col = game.show_play(form='narrow').shape[1]
        self.assertEqual(expect_col, actual_col)
        
        
    def test_face_count(self):
        '''
        Tests the face_counts_roll method.
        '''
        testdie1 = Die([1,2,3])
        testdie2 = Die([1,2,3])
        testdie_lst = ([testdie1, testdie2])
        
        testgame = Game(testdie_lst)
        testgame.play(2)
        test_analyze = Analyzer(testgame)
        test_df = test_analyze.face_count()
        shape = test_df.shape[0]
        expected = 2
        actual = shape
        self.assertEqual(expected, actual)
        

    def test_jp(self):
        '''
        Tests the jackpot method.
        '''
        testdie1 = Die([1,2,3])
        testdie2 = Die([1,2,3])
        testdie3 = Die([1,2,3])
        testdie_lst = ([testdie1, testdie2, testdie3])
        
        testgame = Game(testdie_lst)
        testgame.play(3)
        analyze = Analyzer(testgame)
        jps = analyze.jackpot()
        self.assertTrue(type(jps) == int)
    

    def test_combo(self):
        '''
        Tests the combo method.
        '''
        testdie1 = Die([1,2,3])
        testdie2 = Die([1,2,3])
        testdie3 = Die([1,2,3])
        testdie_lst = ([testdie1, testdie2, testdie3])
        
        testgame = Game(testdie_lst)
        testgame.play(3)
        test_analyze = Analyzer(testgame)
        test_df = test_analyze.combo().size
        self.assertGreater(test_df, 0)
        
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)