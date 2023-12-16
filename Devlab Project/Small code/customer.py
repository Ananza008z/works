while True:
    global n
    n = int(input())
    if n > 0:
        break
    
def calculator(rnd, next_rnd):
    rnd = [a-1 if a != 0 else a for a in rnd]
    rnd = [rnd[d]+next_rnd[d] for d in range(len(next_rnd))]
    return rnd

m = int(input())

data_set = []
for i in range(m):
    data_set.append([int(c) for c in input().split(' ')])
    
base = data_set[0]
for index1, line in enumerate(data_set):
    if index1 == 0:
        print(' '.join([str(a) for a in base]))
        continue
    else:
        base = calculator(base, line)
        print(' '.join([str(a) for a in base]))
        