import math
n = int(input())

data_set = []
for i in range(n):
    data_set.append([int(c) for c in input().split()])

def calculate(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
length = []
while len(data_set) > 0:
    for k in range(1, len(data_set)):
        length.append(calculate(data_set[0], data_set[k]))
    data_set.remove(data_set[0])
print(f"{min(length)**2:.2f}")