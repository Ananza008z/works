n = [str(a) for a in input()]
cmd = [str(c) for c in input()]

for i in cmd:
    if  i == 'L':
        n.remove(n[0])
    elif i == 'R':
        n.reverse()
        n.remove(n[0])
        n.reverse()
right = n.count('(')
left = n.count(')')
if right == left:
    print('NO')
else:
    print('YES')