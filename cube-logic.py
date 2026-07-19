from cube import cube

os = []
for i in range(6):
    os += 9*[i]
x = cube(os)
print("before move:")
for j in range(6):
    print(f"face: {j}")
    for i in range(9*j, 9*(j+1), 3):
        print("".join([str(c) for c in x.cube[i:i+3]]))
x.F()
for j in range(6):
    print(f"face: {j}")
    for i in range(9*j, 9*(j+1), 3):
        print("".join([str(c) for c in x.cube[i:i+3]]))