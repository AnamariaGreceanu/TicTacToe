import unittest
from main import is_found_winner
    
    
class TestWinnerInTable(unittest.TestCase):
    def test_is_winner_on_line(self):
        actual=is_found_winner(table=[[1,2,3],["X","X","X"],[7,0,0]])
        self.assertTrue(actual,"it s not working on line")
    
    def test_is_winner_on_column(self):
        actual=is_found_winner(table=[["X",2,0],[4,"X",0],[7,"X",0]])
        self.assertTrue(actual,"it s not working on column")
    
    def test_is_winner_on_mainDiag(self):
        actual=is_found_winner(table=[["X",2,0],[4,"X",0],[7,8,"X"]])
        self.assertTrue(actual,"it s not working on main Diag")
    
    def test_is_winner_on_secDiag(self):
        actual=is_found_winner(table=[[1,"X",0],[4,0,"X"],[0,"X",9]])
        self.assertTrue(actual,"it s not working on sec Diag")
    
if __name__ == '__main__':
    unittest.main()
# in command line python -m unittest + optional:-v + the file to be run:test.py