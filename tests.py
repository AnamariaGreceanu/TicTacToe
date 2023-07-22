import unittest

def is_winner_on_line(table):
    for i in range(0,3):
        if table[i][0]==table[i][1]==table[i][2]:
            return True
    return False
    
def is_winner_on_column(table):
    for j in range(0,3):
        if table[0][j]==table[1][j]==table[2][j]:
            return True
    return False
    
def is_winner_on_main_diagonal(table):
    if table[0][0]==table[1][1]==table[2][2]:
        return True
    return False
    
def is_winner_on_secondary_diagonal(table):
    if table[0][2]==table[1][1]==table[2][0]: 
        return True
    return False
    
class TestWinnerInTable(unittest.TestCase):
    # def __init__(self, methodName: str = "runTest") -> None:
    #     super().__init__(methodName)
    
    def test_is_winner_on_line(self):
        actual=is_winner_on_line(table=[[1,2,3],["X","X","X"],[7,0,0]])
        self.assertEqual(actual,True,"it s not working on line")
    
    def test_is_winner_on_column(self):
        actual=is_winner_on_column(table=[[1,2,0],[4,"X",0],[0,"X",9]])
        self.assertEqual(actual,False,"it s not working on column")
    
    def test_is_winner_on_mainDiag(self):
        actual=is_winner_on_main_diagonal(table=[["X",2,0],[4,"X",0],[7,8,"X"]])
        self.assertEqual(actual,True,"it s not working on main Diag")
    
    def test_is_winner_on_secDiag(self):
        actual=is_winner_on_secondary_diagonal(table=[[1,"X",0],[4,0,"X"],[0,"X",9]])
        self.assertEqual(actual,True,"it s not working on sec Diag")
    
if __name__ == '__main__':
    unittest.main()
# in command line pyhon -m unittest + optional:-v + the file to be run:test.py