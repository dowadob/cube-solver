class cube:
    def __init__(self, state):
        self.up = state[0]
        self.front = state[1]
        self.down = state[2]
        self.right = state[3]
        self.left = state[4]
        self.back = state[5]
    # move left to down
    def L(self):
        # left side of back in list[0]
        l = None
        l.append([rows_in_back[0] for rows_in_back in self.back])
        l.append([rows_in_up[0] for rows_in_up in self.up])
        l.append([rows_in_front[0] for rows_in_front in self.front])
        l.append([rows_in_down[0] for rows_in_down in self.down])

        for i in range(3):
            self.up[i][0] = l[0][i]
        for i in range(3):
            self.front[i][0] = l[1][i]
        for i in range(3):
            self.down[i][0] = l[2][i]
        for i in range(3):
            self.back[i][0] = l[3][i]
        
        for i in range(3):
            
    # move right to up
    def R(self):
        # right side of front in list[0]
        l = []
        l.append([rows_in_front[0] for rows_in_front in self.front])
        l.append([rows_in_up[0] for rows_in_up in self.up])
        l.append([rows_in_back[0] for rows_in_back in self.back])
        l.append([rows_in_down[0] for rows_in_down in self.down])

        for i in range(3):
            self.up[i][0] = l[0][i]
        for i in range(3):
            self.back[i][0] = l[1][i]
        for i in range(3):
            self.down[i][0] = l[2][i]
        for i in range(3):
            self.front[i][0] = l[3][i]
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
    
