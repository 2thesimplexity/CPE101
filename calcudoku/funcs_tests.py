import unittest
import calcudoku

class TestCases(unittest.TestCase):
    
    def setUp(self):
        
        self.grid = [[4, 1, 2, 5, 3], 
                     [1, 5, 4, 3, 2], 
                     [2, 3, 5, 4, 1], 
                     [3, 4, 1, 2, 5], 
                     [5, 2, 3, 1, 4]]
        
        self.bad_grid = [[4, 1, 2, 5, 3], 
                         [1, 5, 4, 3, 2], 
                         [2, 2, 5, 4, 1], 
                         [3, 4, 1, 2, 5], 
                         [5, 2, 3, 1, 4]]
        
        self.cages = [[5, 2, 0, 5],
                      [8, 3, 1, 2, 6],
                      [8, 2, 3, 8],
                      [6, 3, 4, 9, 14],
                      [13, 3, 7, 12, 13],
                      [5, 2, 10, 15],
                      [14, 4, 11, 16, 20, 21],
                      [6, 3, 17, 18, 22],
                      [10, 3, 19, 23, 24]]
    

    def test_validate_rows(self):
        pass


    def test_validate_cols(self):
        pass
      
    def test_validate_cages(self):
        pass


if __name__ == "__main__":
   unittest.main()

