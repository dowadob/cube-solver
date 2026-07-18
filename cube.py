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
        c = self.cube
        # simpan kolom kiri Up
        t0, t1, t2 = c[0], c[3], c[6]

        # Up <- Back
        c[0], c[3], c[6] = c[35], c[32], c[29]

        # Back <- Down
        c[29], c[32], c[35] = c[51], c[48], c[45]

        # Down <- Front
        c[45], c[48], c[51] = c[9], c[12], c[15]

        # Front <- Up lama
        c[9], c[12], c[15] = t0, t1, t2

        # putar face kiri
        t = c[36:45]

        c[36] = t[6]
        c[37] = t[3]
        c[38] = t[0]
        c[39] = t[7]
        c[40] = t[4]
        c[41] = t[1]
        c[42] = t[8]
        c[43] = t[5]
        c[44] = t[2]
    # move right to up
    def R(self):
        c = self.cube
        # ---------- save Up right column ----------
        t0, t1, t2 = c[2], c[5], c[8]

        # Up <- Front
        c[2], c[5], c[8] = c[11], c[14], c[17]

        # Front <- Down
        c[11], c[14], c[17] = c[47], c[50], c[53]

        # Down <- Back (reversed)
        c[47], c[50], c[53] = c[33], c[30], c[27]

        # Back <- old Up (reversed)
        c[27], c[30], c[33] = t2, t1, t0

        # ---------- rotate Right face clockwise ----------
        t = c[18:27].copy()

        c[18] = t[6]
        c[19] = t[3]
        c[20] = t[0]

        c[21] = t[7]
        c[22] = t[4]
        c[23] = t[1]

        c[24] = t[8]
        c[25] = t[5]
        c[26] = t[2]        
    # move up to right
    def U(self):
        c = self.cube
        #takes front top row
        t0, t1, t2 = c[9], c[10], c[11]
        #modify the front up row
        c[9], c[10], c[11] = c[9*4], c[9*4+1], c[9*4+2]
        #modify the left up row
        c[9*4], c[9*4+1], c[9*4+2] = c[9*3], c[9*3+1], c[9*3+2]
        #modify the back up row
        c[9*3], c[9*3+1], c[9*3+2] =c[9*2], c[9*2+1], c[9*3+1]
        #modify right up row
        c[9*2], c[9*2+1], c[9*3+1] = t0, t1, t2
        #modify the up face
        t0 = c[0]
        c[0] = c[2]
        c[2]=c[8]
        c[8]=c[6]
        t = c[1]
        c[1]=c[5]
        c[5]=c[7]
        c[7]=c[3]
        c[3]=t0