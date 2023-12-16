a = [int(c) for c in input().split()]
b = [int(z) for z in input().split()]

check_a = [0 if i1 > 32548 else 1 for i1 in a]
check_b = [0 if i2 > 32548 else 1 for i2 in b]

if all(check_a) == False or all(check_b) == False:
    print('invalid')
elif len(a) != len(b):
    print('invalid')
else:
    sum_all = [a[i]+b[i] for i in range(len(a))]
    print(' '.join([str(k) for k in sum_all]))