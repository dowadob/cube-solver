from cube import Cube
from copy import deepcopy
from node import Node

c = Cube([i for i in range(6) for _ in range(9)])
c.state = c.B_prime()
c.state = c.U()
c.state = c.F()

frontier, explored = [], []
solution = []
current_state = Node(c, None, None)

while True:
    if current_state.state.isSolved():
        break
    explored.append(current_state.state.state)
    for node in current_state.get_possible_moves():
        if node.state.state not in explored:
            frontier.append(node)
    current_state = frontier[-1]
    print(current_state.move)
    frontier.pop(-1)
n = current_state
while True:
    if n.parent is None:
        break
    solution.insert(0, n.move)
    n = n.parent
if(len(solution) == 0):
    print("cube is solved")
print(' '.join(solution))