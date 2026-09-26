from cube import Cube
class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
    def get_possible_moves(self):
        return [
            Node(Cube(self.state.L()), self, 'L'), 
            Node(Cube(self.state.R()), self, 'R'), 
            Node(Cube(self.state.U_prime()), self, 'U\''), 
            Node(Cube(self.state.F()), self, 'F'), 
            Node(Cube(self.state.D_prime()), self, 'D\''), 
            Node(Cube(self.state.B_prime()), self, 'B\'')
            ]