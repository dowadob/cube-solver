from cube import Cube
from copy import deepcopy

state = [
    2, 0,0,3,0,0,3,2,3,
    0,3,2,0,1,1,1,5,4,
    5,2,1,4,2,0,5,4,5,
    2,3,3,1,3,5,4,1,4,
    0,4,4,3,4,4,0,1,5,
    2,2,3,5,5,5,1,2,1,
]
frontier, explored = [], []
solution = []
current_state = Cube(state)

while True:
    if current_state.isSolved():
        break
    explored.append(current_state)
    frontier += current_state.get_possible_moves()
    current_state = frontier[-1]
    dfrontier.pop(-1)

n = current_state
while True:
    if n.parent is None:
        break
    solution.insert(0, n.move)
    n = n.parent
if(len(solution) == 0):
    print("cube is solved")
print(' '.join(solution))