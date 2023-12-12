def process(vertical1, horizontal1, b1):
    for check_row in horizontal1:
        if len(check_row) != len(set(check_row)):
            return False
    for check_col in vertical1:
        if len(check_col) != len(set(check_col)):
            return False
    for check_block in b1:
        if len(check_block) != len(set(check_block)):
            return False
        
    return True

sudoku = []

for _ in range(9):
    sudoku.append([int(c) for c in input().split(' ')])


horizontal = []
t_vertical = []
vertical = []
t_block = []
for k in sudoku:
    horizontal.append([c for c in k if c != 0])

for row in range(9):
    sublst = []
    for col in range(9):
        sublst.append(sudoku[col][row])
    t_vertical.append(sublst)

for del_0 in t_vertical:
    vertical.append([c for c in del_0 if c != 0])

t_block = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        group = [sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        t_block.append(group)

block = []

for del_0_b in t_block:
    block.append([c for c in del_0_b if c != 0])
state = process(vertical, horizontal, block)

print(state)
