ckr = 0
nd = 0

lst = []

for i in range(4):
    k = str(input().capitalize())
    if k == 'Chicken rice':
        lst.append(k)
        ckr += 1
    else:
        lst.append(k)
        nd += 1
if ckr > nd: print('Chiken rice')
elif nd > ckr: print('Noodle')
else:print(lst[2])