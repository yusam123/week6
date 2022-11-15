import random
class Game():
    def __init__(self):
        self.board = []
        self.winner = None
        self.mode = None
        pass

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""

        for i in range(3):
            verticle_flag = ''
            parrelle_flag = ''
            for j in range(3):
                verticle_flag = verticle_flag +str(board[i][j])
                parrelle_flag = parrelle_flag + str(board[j][i])
        
            if parrelle_flag  == "OOO" or verticle_flag == "OOO":
                return "O"
            if parrelle_flag == "XXX" or verticle_flag == "XXX":
                return "X"
            
        diagonal_flag = str(board[0][0])+str(board[1][1])+str(board[2][2])
        rdiagonal_flag = str(board[2][0])+str(board[1][1])+str(board[0][2])
        if diagonal_flag == "OOO" or rdiagonal_flag == "OOO":
            return "O"
        if diagonal_flag == "XXX" or rdiagonal_flag == "XXX":
            return "X"

        return None  

    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player == "O":
            return "X"
        if player == "X":
            return "O"
    

class People(Game):
    def __init__(self,role):
        super().__init__()
        self.role = role

    def input_position(self,position,board):
        self.board = board
        self.board[int(position[1])-1][int(position[3])-1] = self.role
        return self.board

class Computer(Game):
    def __init__(self,role):
        super().__init__()
        self.role = role

    def random_input(self,board):
        self.board = board
        x = random.randint(0,2)
        y = random.randint(0,2)
        while self.board[x][y] != None:
             x = random.randint(0,2)
             y = random.randint(0,2)
        self.board[x][y] = self.role
        return self.board