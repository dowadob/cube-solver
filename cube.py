class cube:
    """
    colors: 0 yellow, 1 red, 2 green, 3 orange, 4 blue, 5 white
    faces: index 0-8 up, 9*1 front, 9*2-.. right, 9*3 back, 9*4 left, 9*5-53 down
    colors in face : 0 up left, 2up middle, 3 up right, 4 middle left, 5 middle middle, .... down right
    faces perspective: from Front side, turn right to see right side, turn right to see back side, turn right to see left side
    from Front side, turn up to see up side, turn down twice to see down side
    right side in Front, right side in Up, right side in Down, and left side in Back are in the same layer
    top side in Front, top side in back, top side in left, top side in right are in the same layer
    every moves executed in Front perspective
    state takes list[54] of integers for now
    """
    def __init__(self, state):
        self.cube = state
    # move left to down
    def L(self):
        # right side of back reversed which become left side in UP
        l = []
        l += self.cube[9*3+2:9*4:3][::-1]
        # left side of Up which become left side in front
        l += self.cube[0:9:3]
        #left side of front which become  left side in Down
        l += self.cube[9:9*2:3]
        #left side of down reversed which become right side in back
        l += self.cube[9*5:54:3][::-1]

        #left side in up
        for i in range(0, 9, 3):
            self.cube[i] = l[0]
            l.pop(0)
        #left side of Front
        for i in range(9, 9*2,3):
            self.cube[i] = l[0]
            l.pop(0)
        #left side of Down
        for i in range(9*5,54,3):
            self.cube[i] = l[0]
            l.pop(0)
        #right side in back
        for i in range(9*3+2,9*4, 3):
            self.cube[i] = l[0]
            l.pop(0)
        
    # move right to up
    def R(self):
        # right side of front which become right side in UP
        l = []
        l += self.cube[9+2:9*2:3]
        # right side of Up reversed which become left side in back
        l += self.cube[2:9:3][::-1]
        #left side of back reversed which become  right side in Down
        l += self.cube[9*3:9*4:3][::-1]
        #right side of down which become right side in front
        l += self.cube[9*5:54:3][::-1]

        #left side in up
        for i in range(0, 9, 3):
            self.cube[i] = l[-1]
            l.pop(-1)
        #left side of Front
        for i in range(9, 9*2,3):
            self.cube[i] = l[-1]
            l.pop(-1)
        #left side of Down
        for i in range(9*5,54,3):
            self.cube[i] = l[-1]
            l.pop(-1)
        #right side in back
        for i in range(9*3+2,9*4, 3):
            self.cube[i] = l[-1]
            l.pop(-1)
        
    # move up to right
    def U(self):
        #first row of left in l[0]
        l = []
        l.append([col for col in self.left[0]])
        l.append([col for col in self.front[0]])
        l.append([col for col in self.right[0]])
        l.append([col for col in self.back[0]])

        for i in range(3):
            self.up[i][0] = l[0][i]
        for i in range(3):
            self.back[i][0] = l[1][i]
        for i in range(3):
            self.down[i][0] = l[2][i]
        for i in range(3):
            self.front[i][0] = l[3][i]
    
